$( document ).ready(function() {

    var geojsonLayer;
    

	$("#refresh").click( function () {
	    getData();
	})

	L.mapbox.accessToken = 'pk.eyJ1IjoiaGFyYmllaXNtIiwiYSI6IksyU1Rkc0UifQ.eXciAIxM0pfdj5STBHNnbQ';

	var map = L.mapbox.map('map', 'harbieism.k45k1ejj');

	navigator.geolocation.getCurrentPosition(function(position) {
	  userLat = position.coords.latitude;
	  userLng = position.coords.longitude;
	  map.setView([userLat, userLng], 9)

	  	var userMarker = L.marker(new L.LatLng(userLat, userLng), {
		    icon: L.mapbox.marker.icon({
		        'marker-color': 'ff8888'
		    }),
		    draggable: true
		});

		userMarker.addTo(map);
	});


	var getData = (function() {
		$.get( 'get.geojson.js', function(data) {
			geojsonLayer = L.geoJson(data, {
				onEachFeature: function(feature, layer) {
					layer.bindPopup(feature.properties.location);
				}
		    })
		    geojsonLayer.addTo(map);
		});
    });
    
	getData();


});