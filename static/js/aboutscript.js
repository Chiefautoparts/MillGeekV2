'use strict';

navBox = document.getElementById('navBox');
navButton = document.getElementById('navButton');

navBox.style.display = 'none';
navButton.addEventListener('click', displayBox);
navBox.addEventListener('mouseleave', hideBox);

function displayBox() {
	if (navBox.style.display === 'none') {
		navBox.setAttribute('style', 'display: block');
	} else {
		navBox.style.display = 'none';
	}
}

function hideBox() {
	navBox.setAttribute('style', 'display: none');
}