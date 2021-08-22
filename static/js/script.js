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
});

