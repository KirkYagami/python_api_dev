from flask import Flask, request, jsonify, g
import time
from collections import defaultdict
import threading

app = Flask(__name__)

class RequestCounterMiddleware:
    """Middleware to count API requests per user"""
    
    def __init__(self):
        self.request_counts = defaultdict(int)
        self.lock = threading.Lock()
    
    def _get_user_identifier(self):
        """Extract user identifier from request"""
        # 1. Check API Key in Authorization header
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            api_key = auth_header[7:17]
            return f"api_key_{api_key}"
        
        # 2. Check for user_id in query parameters
        user_id = request.args.get('user_id')
        if user_id:
            return f"user_{user_id}"
        
        # 3. Use IP address as fallback
        ip = request.remote_addr or 'unknown'
        return f"ip_{ip}"
    
    def before_request(self):
        """Called before each request"""
        try:
            g.request_start_time = time.time()
            g.user_identifier = self._get_user_identifier()
            
            with self.lock:
                self.request_counts[g.user_identifier] += 1
                g.request_count = self.request_counts[g.user_identifier]
        except Exception as e:
            print(f"Error in before_request: {e}")
            # Set defaults to prevent errors
            g.request_start_time = time.time()
            g.user_identifier = 'error'
            g.request_count = 0
    
    def after_request(self, response):
        """Called after each request"""
        try:
            # Add custom headers
            if hasattr(g, 'request_count'):
                response.headers['X-Request-Count'] = str(g.request_count)
            if hasattr(g, 'user_identifier'):
                response.headers['X-User-Identifier'] = g.user_identifier
            
            # Log the request
            if hasattr(g, 'request_start_time'):
                processing_time = time.time() - g.request_start_time
                user_id = getattr(g, 'user_identifier', 'unknown')
                count = getattr(g, 'request_count', 0)
                print(f"[{time.ctime()}] {user_id} - "
                      f"{request.method} {request.path} - "
                      f"Count: {count} - Time: {processing_time:.2f}s")
        except Exception as e:
            print(f"Error in after_request: {e}")
        
        return response
    
    def get_statistics(self):
        """Get request statistics"""
        with self.lock:
            total_requests = sum(self.request_counts.values())
            top_users = sorted(
                self.request_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )[:5]
            
            return {
                'total_requests': total_requests,
                'unique_users': len(self.request_counts),
                'top_users': dict(top_users)
            }
    
    def reset(self):
        """Reset all statistics"""
        with self.lock:
            self.request_counts.clear()

# Initialize and register middleware
middleware = RequestCounterMiddleware()
app.before_request(middleware.before_request)
app.after_request(middleware.after_request)

# API Routes
@app.route('/')
def home():
    return jsonify({
        'message': 'Flask API with Request Counting',
        'endpoints': {
            '/api/data': 'GET - Sample data',
            '/api/users': 'POST - Create user',
            '/api/stats': 'GET - Request statistics',
            '/api/reset-stats': 'POST - Reset statistics'
        }
    })

@app.route('/api/data')
def get_data():
    return jsonify({
        'data': ['item1', 'item2', 'item3'],
        'timestamp': time.time()
    })

@app.route('/api/users', methods=['POST'])
def create_user():
    user_data = request.get_json() or {}
    return jsonify({
        'message': 'User created successfully',
        'user': user_data,
        'id': 123
    }), 201

@app.route('/api/stats')
def get_stats():
    return jsonify(middleware.get_statistics())

@app.route('/api/reset-stats', methods=['POST'])
def reset_stats():
    middleware.reset()
    return jsonify({'message': 'Statistics reset successfully'})

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    print(f"500 Error: {error}")
    return jsonify({'error': 'Internal server error', 'details': str(error)}), 500

if __name__ == '__main__':
    print("Starting Flask API with Request Counting Middleware...")
    print("\nAvailable endpoints:")
    print("  GET  /")
    print("  GET  /api/data")
    print("  POST /api/users")
    print("  GET  /api/stats")
    print("  POST /api/reset-stats")
    print("\nRunning on http://127.0.0.1:5000")
    print("-" * 50)
    app.run(debug=True, port=5000, use_reloader=False)
    