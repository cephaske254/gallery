$(document).ready(function () {
    $('span.full-screen').click(function () {
        let target = $(this).parent().parent().parent().parent()
        target.toggleClass("full col-sm-12  col-md-12  col-lg-12")
    })

    $('span.copy-link').click(function () {
        let target = $(this).parent().parent().parent().parent()
        target.toggleClass("full col-sm-12  col-md-12  col-lg-12")
    })

    $('.photo-cont').hover(function () {
        if (!$(this).hasClass('full')) {
            $(this).find('.controls, .caption').fadeIn().css({ 'display': 'flex', 'text-align': 'center' })
        }
    },
        function () {
            if (!$(this).hasClass('full')) {
                $(this).find('.controls, .caption').slideUp()
            }
        })

    

    // auto dissmiss alert
    window.setTimeout(function () {
        $(".alert").slideUp(500, function () {
            $(this).remove();
        });
    },2500)


})