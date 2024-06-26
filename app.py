from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize an empty list to store tasks
tasks = []

# Route for rendering the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Flask route for adding a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    task_content = data['task_content']
    tasks.append({'content': task_content, 'completed': False})
    return jsonify({'status': 'success', 'message': 'Task added successfully'})


# Route for marking a task as completed
@app.route('/complete_task', methods=['POST'])
def complete_task():
    data = request.get_json()
    task_content = data['task_content']
    for task in tasks:
        if task['content'] == task_content:
            task['completed'] = True
            break
    return jsonify({'status': 'success', 'message': 'Task completed successfully'})

# Route for deleting a task
@app.route('/delete_task', methods=['POST'])
def delete_task():
    data = request.get_json()
    task_content = data['task_content']
    for task in tasks:
        if task['content'] == task_content:
            tasks.remove(task)
            break
    return jsonify({'status': 'success', 'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
