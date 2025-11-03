import requests
import time
import json

BASE_URL = "http://localhost:5000"

def print_separator():
    print("\n" + "="*60 + "\n")

def test_requests():
    print("Testing Flask API with Request Counter Middleware")
    print_separator()
    
    # Test 1: User with API Key
    print("TEST 1: User with API Key")
    headers1 = {'Authorization': 'Bearer user1_api_key_12345'}
    try:
        response1 = requests.get(f"{BASE_URL}/api/data", headers=headers1)
        print(f"Status Code: {response1.status_code}")
        print(f"Request Count: {response1.headers.get('X-Request-Count')}")
        print(f"User Identifier: {response1.headers.get('X-User-Identifier')}")
        print(f"Response: {json.dumps(response1.json(), indent=2)}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to server. Is Flask running?")
        return
    
    print_separator()
    
    # Test 2: User with query parameter
    print("TEST 2: User with query parameter")
    response2 = requests.get(f"{BASE_URL}/api/data?user_id=alice")
    print(f"Status Code: {response2.status_code}")
    print(f"Request Count: {response2.headers.get('X-Request-Count')}")
    print(f"User Identifier: {response2.headers.get('X-User-Identifier')}")
    print(f"Response: {json.dumps(response2.json(), indent=2)}")
    
    print_separator()
    
    # Test 3: User identified by IP only
    print("TEST 3: User identified by IP (no auth/user_id)")
    response3 = requests.get(f"{BASE_URL}/api/data")
    print(f"Status Code: {response3.status_code}")
    print(f"Request Count: {response3.headers.get('X-Request-Count')}")
    print(f"User Identifier: {response3.headers.get('X-User-Identifier')}")
    
    print_separator()
    
    # Test 4: Multiple requests from same user
    print("TEST 4: Multiple requests from same user (alice)")
    for i in range(3):
        response = requests.get(f"{BASE_URL}/api/data?user_id=alice")
        print(f"Request {i+1} - Count: {response.headers.get('X-Request-Count')}")
    
    print_separator()
    
    # Test 5: POST request
    print("TEST 5: POST request to create user")
    user_data = {"name": "Bob", "email": "bob@example.com"}
    response5 = requests.post(
        f"{BASE_URL}/api/users?user_id=bob",
        json=user_data
    )
    print(f"Status Code: {response5.status_code}")
    print(f"Request Count: {response5.headers.get('X-Request-Count')}")
    print(f"Response: {json.dumps(response5.json(), indent=2)}")
    
    print_separator()
    
    # Test 6: Check statistics
    print("TEST 6: Request statistics")
    stats_response = requests.get(f"{BASE_URL}/api/stats")
    print(f"Status Code: {stats_response.status_code}")
    print(f"Statistics:\n{json.dumps(stats_response.json(), indent=2)}")
    
    print_separator()
    
    # Test 7: Test different API keys
    print("TEST 7: Different API keys")
    headers_a = {'Authorization': 'Bearer key_abc_123456'}
    headers_b = {'Authorization': 'Bearer key_xyz_789012'}
    
    for i in range(2):
        resp_a = requests.get(f"{BASE_URL}/api/data", headers=headers_a)
        print(f"Key A - Count: {resp_a.headers.get('X-Request-Count')}")
        
        resp_b = requests.get(f"{BASE_URL}/api/data", headers=headers_b)
        print(f"Key B - Count: {resp_b.headers.get('X-Request-Count')}")
    
    print_separator()
    
    # Test 8: Final statistics
    print("TEST 8: Final statistics after all tests")
    final_stats = requests.get(f"{BASE_URL}/api/stats")
    stats = final_stats.json()
    print(f"Total Requests: {stats['total_requests']}")
    print(f"Unique Users: {stats['unique_users']}")
    print(f"Top Users:")
    for user, count in stats['top_users'].items():
        print(f"  {user}: {count} requests")
    
    print_separator()
    
    # Test 9: Test reset (optional)
    print("TEST 9: Reset statistics")
    reset_response = requests.post(f"{BASE_URL}/api/reset-stats")
    print(f"Reset Status: {reset_response.status_code}")
    print(f"Message: {reset_response.json()['message']}")
    
    # Verify reset
    verify_stats = requests.get(f"{BASE_URL}/api/stats")
    print(f"Stats after reset: {json.dumps(verify_stats.json(), indent=2)}")
    
    print_separator()
    print("All tests completed!")

def test_error_handling():
    """Test error handling"""
    print("\nTesting error handling...")
    
    # Test 404
    response = requests.get(f"{BASE_URL}/api/nonexistent")
    print(f"404 Test - Status: {response.status_code}, Response: {response.json()}")

if __name__ == "__main__":
    try:
        test_requests()
        test_error_handling()
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Could not connect to Flask server!")
        print("Make sure the Flask app is running on http://localhost:5000")
        print("Run: python app.py")
    except KeyboardInterrupt:
        print("\n\nTests interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")