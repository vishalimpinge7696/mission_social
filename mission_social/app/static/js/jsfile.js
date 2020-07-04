 $(document).ready(function() {
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll > 100) {
            $(".header").css("background", "white");
            $(".blcl").css("color", "black");
        } else {
            $(".header").css("background", "rgb(0,0,0,0)");
            $(".blcl").css("color", "white");
        }
    });
})