'use strict';

function initMap() {
	var uluru = {lat: -47.8349, lng: 122.2121};
	var map = new google.maps.Map(document.getElementById('map'), {
		room: 4,
		center: uluru
	});
	var marker = new google.maps.Marker({
		position: uluru,
		map: map
	});
}