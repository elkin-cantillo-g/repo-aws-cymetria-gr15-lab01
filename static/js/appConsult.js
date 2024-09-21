function consult_user(){
    Task_id = document.getElementById('Task_id').value
    fetch('/consult_user', {
        "method":"post",
        "headers":{"Content-Type":"application/json"},
        "body": JSON.stringify(Task_id)
    })
    .then(resp => resp.json())
    .then(data => {
        document.getElementById("txt-response").value = " Task Id: " + data.Task_id + " Id Employee: " + data.id_employee + " LastName: " + data.lastname + " FirstName: " + data.firstname + " Task Text: " + data.task_text + " Task Date: " + data.task_date + " Task Date Currently: " + data.task_date_currently
    })
}
