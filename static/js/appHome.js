document.querySelector("#btn-register").addEventListener('click', register_view)
document.querySelector("#btn-consult").addEventListener('click', consult_view)
document.querySelector("#btn-delete").addEventListener('click', delete_view)
document.querySelector("#btn-update").addEventListener('click', update_view)

function register_view () {
    window.location = "/register_page"
}

function consult_view () {
    window.location = "/consult_page"
}

function delete_view () {
    window.location = "/delete_page"
}

function update_view () {
    window.location = "/update_page"
}
