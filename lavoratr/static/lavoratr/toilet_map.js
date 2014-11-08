L.mapbox.accessToken = 'pk.eyJ1IjoiaGFyYmllaXNtIiwiYSI6IksyU1Rkc0UifQ.eXciAIxM0pfdj5STBHNnbQ';

var map = L.mapbox.map('map', 'harbieism.k45k1ejj').setView([40, -74.50], 9);

map.on('moveend', function(e){
	var bounds = map.getBounds();
	var southWest = bounds.getSouthWest();
	var northEast = bounds.getNorthEast();
	var boundObject = {
		southWestLat: southWest.lat,
		southWestLng: southWest.lng,
		northEastLat: northEast.lat,
		northEastLng: northEast.lng,
	}
	$.get( 'get.geojson.js', boundObject, function(data) {
		L.geoJson(data, {
			onEachFeature: function(feature, layer) {
				layer.bindPopup(feature.properties.location);
			}
		}).addTo(map);
    });

});


