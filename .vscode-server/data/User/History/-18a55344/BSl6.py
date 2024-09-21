from flask import render_template, request, jsonify
from server import app
from database.db import *
from controllers.admin_s3 import *

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/consult_page')
def register_page():
    return render_template("consult.html")

@app.route('/register_user', methods=["post"])
def register_user():
    data = request.form
    file = request.file
    id_employee, lastname, firstname, task_text, task_date = data["id_employee"], data["lastname"], data["firstname"],data["task_text"] ,data["task_date"]
    insert(id_employee, lastname, firstname, task_text, task_date)
    session_s3 = connectionS3()
    photo_path, photo_name = save_file(id_employee, photo)
    upload_file_s3(session_s3, photo_path, photo_name)
    
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

@app.route('/consult_user', methods=["post"])
def consult_user():
    id = request.get_json()
    result = consult(id)
    resp_data = {
            'name': result[0][1],
            'lastname': result[0][2],
            'birthday': result[0][3]
            }

    return jsonify(resp_data)
