from flask import Flask, render_template, request
from database.db import *

app = Flask(__name__)

@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/register_user', methods=["post"])
def register_user():
    data = request.form
    id_employee, lastname, firstname, task_text, task_date = data["id_employee"], data["lastname"], data["firstname"],data["task_text"] ,data["task_date"]
    insert(id_employee, lastname, firstname, task_text, task_date)
    return "Task added"

@app.route('/delete_user', methods=["post"])
def delete_user():
    data = request.form
    Task_id, id_employee = data["Task_id"], data["id_employee"]
    delete(Task_id, id_employee)
    return "Task deleted"

@app.route('/update_user', methods=["post"])
def update_user():
    data = request.form
    Task_id, id_employee, lastname, firstname, task_text, task_date = data["Task_id"], data["id_employee"], data["lastname"], data["firstname"],data["task_text"] ,data["task_date"]
    update(Task_id,id_employee, lastname, firstname, task_text, task_date)
    return "Task Updated"

if __name__ == "__main__":    
    host = "172.31.29.219"
    port = 80
    app.run(host, port, True)
