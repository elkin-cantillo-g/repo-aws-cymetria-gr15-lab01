import pymysql

host = "rds-mysql-aws-cymetria-gr15-lab02.chq2i2wisw35.us-east-2.rds.amazonaws.com"
user = "admin"
passw = "yn62GJ4iKfuiNBYzxwwr"
db_name = "db_tasks_employees"

def connection_SQL():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=passw,
            database=db_name
        )
        print("Successful database connectivity")
        return connection
    except Exception as err:
        print("Error", err)
        return None

def insert(id_employee, lastname, firstname, task_text, task_date):
    try:
        instruction = "INSERT INTO tasks_users (id_employee, lastname, firstname, task_text, task_date) VALUES ("+id_employee+", '"+lastname+"', '"+firstname+"', '"+ task_text +"' ,'"+task_date+"');"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print("Task added")
    except Exception as err:
        print("Error", err)
        return None

def delete(Task_id, id_employee):
    try:
        instruction = "DELETE FROM tasks_users WHERE Task_id = "+Task_id+" and id_employee="+id_employee+";"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print(instruction)
        print("Task deleted")
    except Exception as err:
        print("Error", err)
        return None

def update(Task_id, id_employee,lastname, firstname, task_text, task_date):
    try:
        instruction = "UPDATE tasks_users SET lastname = '"+lastname+"', firstname = '"+firstname+"', task_text = '"+task_text+"', task_date ='"+task_date+"' WHERE Task_id = "+Task_id+" and id_employee="+id_employee+";"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print(instruction)
        print("Task updated")
    except Exception as err:
        print("Error", err)
        return None

def consult(Task_id):
    try:
        instruction = "SELECT * FROM tasks_users WHERE Task_id=" + Task_id + ";"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        result = cursor.fetchall()
        print(instruction)
        print("Task consulted")
        return result
    except Exception as err:
        print("Error", err)
        return None
