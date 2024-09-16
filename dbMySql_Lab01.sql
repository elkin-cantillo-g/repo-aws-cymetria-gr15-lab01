CREATE DATABASE db_tasks_employees;

USE db_tasks_employees;

CREATE TABLE tasks_users (
	Task_id INT NOT NULL AUTO_INCREMENT,
	id_employee INT NOT NULL,
	lastname VARCHAR(100) NOT NULL, 
	firstname VARCHAR(100),
	task_text VARCHAR(255) NOT NULL,
	task_date DATE,
	task_date_currently DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (Task_id)
)



