'use strict';

var navBox = document.getElementById('nav-box');
var navBtn = document.getElementById('nav-Btn');

function showNav(){
	
	navBox.style.display = 'none';
	navBtn.addEventListener('click', displayBox);

	function displayBox() {
		if (navBox.style.display === 'none') {
			navBox.setAttribute('style', 'display: block')
		}
		else {
			navBox.style.display = 'none';
		}
	};
}