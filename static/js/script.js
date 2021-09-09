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
    underlineWordInUse();
});

function customHomePageReturn() {
    if (window.location.pathname == "/home_page") {
        $(".home-button-container").html(`<a class="text-shadow return-home-button" href="#">
            Back to Top <i class="fas fa-arrow-up"></i>
        </a>`);
    }
}

function underlineWordInUse() {
    let wordToUnderlineLower = $(".word-name").text().toLowerCase();
    let wordToUnderlineCap = $(".word-name").text();
    if ($('p').hasClass("single-word-use")) {
        let newStringLower = $('.single-word-use').text().replace(`${wordToUnderlineLower}`, `<span class="given-word">${wordToUnderlineLower}</span>`);
        let newString = newStringLower.replace(`${wordToUnderlineCap}`, `<span class="given-word">${wordToUnderlineCap}</span>`);

        $('.single-word-use').html(newString);
    }
    if ($('ul').hasClass("uses-list")){
        let newListLower = $(".uses-list").html().replace(`${wordToUnderlineLower}`, `<span class="given-word">${wordToUnderlineLower}</span>`);
        let newList = newListLower.replace(`${wordToUnderlineCap}`, `<span class="given-word">${wordToUnderlineCap}</span>`);
        $(".uses-list").html(newList);
    }
    
    
}
