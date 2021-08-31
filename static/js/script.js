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
    boldWordInUse();
});

function customHomePageReturn() {
    if (window.location.pathname == "/home_page") {
        $(".home-button-container").html(`<a class="text-shadow return-home-button" href="#">
            Back to Top <i class="fas fa-arrow-up"></i>
        </a>`)
    }
}

function boldWordInUse() {
    let wordToBoldLower = $(".word-name").text().toLowerCase();
    let wordToBoldCap = $(".word-name").text();
    if ($('p').hasClass("single-word-use")) {
        let newString = $('.single-word-use').text().replace(`${wordToBoldLower}!"`, `<span class="given-word">${wordToBoldLower}</span>`)
        $('.single-word-use').html(newString)
    }
}

// for (var i = 0; i <= items.length; i++) {
    //     if (items[i].hasClass()) {
    //         console.log("thank fuck")
    //     } 
    // }
    //    if (Element.hasClass('word-use')) {
    //        console.log("hasclass")
    //        wordUses.push(Element.text())
    //    }
    //    console.log(wordUses)


    // if (wordUse.includes(wordToBoldLower)) {
    //     wordUse.replace(`${wordToBoldLower}`, "por que no")
    //     $(".word-use").text(`${wordUse}`)
    //     console.log("success")
    // } else {
    //     console.log("fail")
    // }