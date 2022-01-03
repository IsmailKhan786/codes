var randomNumber1 = Math.floor(Math.random() *2 ) + 1;
var randomNumber2 = Math.floor(Math.random() * 2) + 1;

var tossImage1 = "headtail" + randomNumber1 + ".jpg";
var tossImage2 = "headtail" + randomNumber2 + ".jpg";

var img1 = document.querySelectorAll("img")[0].setAttribute("src",tossImage1);
var img2 = document.querySelectorAll("img")[1].setAttribute("src",tossImage2);

function Refresh() {
    window.parent.location = window.parent.location.href;
}