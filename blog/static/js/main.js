$(document).ready(function () {
    // if (jQuery) {
    //     // jQuery is loaded  
    //     alert("Yeah!");
    // } else {
    //     // jQuery is not loaded
    //     alert("Doesn't Work");
    // }
    $('.comment-form-trigger').click(function () {
        $(this).next('.comment-form').toggle("slide");
        return false;
    });
    $('.reply-form-trigger').click(function () {
        $(this).next('.reply-form').toggle("slide");
        return false;
    });
});
