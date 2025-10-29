import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
	"""
	Home page with API information.
	"""
	return jsonify({
		'message': 'Welcome to Todo API',
		'endpoints': {
		'GET /tasks': 'Get all tasks',
		'GET /tasks/<id>': 'Get a specific task',
		'POST /tasks': 'Create a new task',
		'PUT /tasks/<id>': 'Update a task',
		'PATCH /tasks/<id>/toggle': 'Toggle task completion',
		'DELETE /tasks/<id>': 'Delete a task'
		}
		})

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row # allows to access columns by name
    return conn


# CRUD

@app.route('/tasks')
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()

    tasks_list = []
    for task in tasks:
        tasks_list.append({
            'id':task['id'],
            'title': task['title'],
            'description': task['description'],
	        'completed': bool(task['completed']),
	        'created': task['created']
        })

    # Return as JSON
    return jsonify(tasks_list)



@app.route('/task/<int:task_id>')
def get_task(task_id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?',
	   (task_id,)).fetchone()
    conn.close()

    if task is None:
	    return jsonify({'error': 'Task not found'}), 404
    
    task_dict = {
        'id': task['id'],
        'title': task['title'],
        'description': task['description'],
        'completed': bool(task['completed']),
        'created': task['created']
        }

    return jsonify(task_dict)


# add new task

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    if not data or 'title' not in data:
          return jsonify({'error': 'Title is required'}), 400

    title = data['title']
    description = data['description']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO tasks( title, description)
                VALUES (?, ?)
                ''', (title, description ))
    
    conn.commit()
    # id of the newly created task
    new_task_id = cur.lastrowid

    return jsonify({
         'message': 'Task created successfully',
         'task_id': new_task_id
    }), 201




## UPDATE

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    conn = get_db_connection()
    # Check if task exists
    task = conn.execute('SELECT * FROM tasks WHERE id = ?',
        (task_id,)).fetchone()
    
    if task is None:
         return jsonify({'error': 'Task not found'}), 404
    title = data.get('title', task['title'])
    description = data.get('description', task['description'])

    conn.execute('''
                UPDATE tasks SET title = ?, description = ? WHERE id = ?
                 ''', (title, description, task_id))
    
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task updated successfully'})

    
## TODO: PATCH:- Implement the logic to complete the task: set completed to 1


@app.route('/tasks/<int:task_id>/toggle', methods=['PATCH'])
def toggle_task(task_id):
    """
    Toggle task completion status.
    """
    conn = get_db_connection()

    # Get current task
    task = conn.execute('SELECT * FROM tasks WHERE id = ?',
    (task_id,)).fetchone()

    if task is None:
        conn.close()
        return jsonify({'error': 'Task not found'}), 404

    # Toggle completed status
    new_status = 0 if task['completed'] else 1

    conn.execute('UPDATE tasks SET completed = ? WHERE id = ?',
    (new_status, task_id))
    conn.commit()
    conn.close()

    return jsonify({
    'message': 'Task status updated',
    'completed': bool(new_status)
    })



## DELETE
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Delete a task from the database.
    """
    conn = get_db_connection()

    # Check if task exists
    task = conn.execute('SELECT * FROM tasks WHERE id = ?',
        (task_id,)).fetchone()

    if task is None:
        conn.close()
        return jsonify({'error': 'Task not found'}), 404

    # Delete task
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': f'Task "{task["title"]}" deleted successfully'})

if __name__=='__main__':
    app.run(debug=True)


