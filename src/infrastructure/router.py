from flask import Flask, redirect, render_template, request, url_for

from src.interfaces.controller.todo_controller import TodoController
from src.infrastructure.sqlite3_handler import db_session


app = Flask(__name__)

todo = TodoController(db_session)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/', methods=['GET', 'PUT', 'DELETE'])
def index():
    result = todo.view()
    return render_template('index.html', data=result)

@app.route('/api/add', methods=['POST', 'GET'])
def add_todo():
    data = request.form
    todo.create(data)
    return redirect(url_for('index'))

@app.route('/api/update', methods=['PUT'])
def update_todo():
    data = request.form
    todo.update(data)
    return redirect(url_for('index'))

@app.route('/api/is_done', methods=['POST'])
def is_done():
    print('is_done')
    return redirect(url_for('index'))

@app.route('/api/delete', methods=['DELETE'])
def delete_todo():
    data = request.form
    todo.remove(data)
    return redirect(url_for('index'))