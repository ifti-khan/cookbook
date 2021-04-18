$(document).ready(function(){
    $("#copyright-jsyear").text(new Date().getFullYear());
    $(".sidenav").sidenav({ edge: "right" });
    $('.modal').modal();
    $('input#input_text, textarea#textarea1, textarea#textarea2').characterCounter();
    $('select').formSelect();
});