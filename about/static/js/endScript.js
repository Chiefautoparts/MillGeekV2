["animationend", "webkitAnimationEnd"].forEach(function(endAnimation) {
	var div = document.getElementsByClassName('homeButton');
	div.addEventListener(endAnimation, newClass, false);
});

function newClass() {
	this.insertAdjacentHTML('afterend',"<div class='show'><a href='/'>Home</a></div>");
	this.className = "new";
}