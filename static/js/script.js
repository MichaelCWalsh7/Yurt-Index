$(document).ready(function () {
    $('.modal').modal();
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('.datepicker').datepicker();
    $('.tabs').tabs();
});

var password = document.getElementById("password"),
    confirm_password = document.getElementById("confirm_password");

var email = document.getElementById("email"),
    confirm_email = document.getElementById("confirm_email");

function validatePassword() {
    if (password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_password.setCustomValidity('');
    }
}

function validateEmail() {
    if (email.value != confirm_email.value) {
        confirm_email.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_email.setCustomValidity('');
    }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;
email.onchange = validateEmail;
confirm_email.onkeyup = validateEmail;