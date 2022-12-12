$(document).ready(function () {
  setTimeout(function () {
    $(".js-alert ").fadeOut("slow", function () {
      $(this).alert("close");
    });
  }, 5000);
});
