$(document).ready(function () {
    $('.modal').modal();
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('.datepicker').datepicker({
        showClearBtn: true,
        yearRange: [1900, 2006],
        format: "dd-mmm-yy"
      });
    $('.tabs').tabs();
    $('.dropdown-trigger').dropdown();
    $('select').formSelect();
    $('.tooltipped').tooltip();

    $('#date_of_birth').bind("click", function() {
        $('#date_of_birth').css("opacity", "1");
    });

    customHomePageReturn();
});

function customHomePageReturn() {
    if (window.location.pathname == "/home_page") {
        $(".home-button-container").html(`<a class="text-shadow return-home-button" href="#">
            Back to Top <i class="fas fa-arrow-up"></i>
        </a>`)
    }
}
