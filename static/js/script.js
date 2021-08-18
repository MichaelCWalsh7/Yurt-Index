$(document).ready(function () {
    $('.modal').modal();
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('.datepicker').datepicker();
    $('.tabs').tabs();
    $('.dropdown-trigger').dropdown();
});

// $("#unrate-link-up").on("click", disableLink)
// $("#not-rated-up").on("click", disableLink)

// function disableLink() {
//     // Finds the id of the clicked button
//     let clickedId = this.id

//     // Disables the button to avoid duplicate liking
//     $(`#${clickedId}`).attr("disabled","disabled");
//     console.log(this.id.toString())   
// }