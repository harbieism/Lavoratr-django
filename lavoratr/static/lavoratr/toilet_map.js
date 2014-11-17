$(document).ready(function() {

    var geojsonLayer;
    var modal = "<a href='#get_modal_data_{}' class='btn btn-lg btn-success'data-toggle='modal'data-target='#basicModal'>Click to open Modal</a>";

	$("#refresh").click( function () {
		geojsonLayer.clearLayers();
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

	if (!String.prototype.format) {
	  String.prototype.format = function() {
	    var args = arguments;
	    return this.replace(/{(\d+)}/g, function(match, number) { 
	      return typeof args[number] != 'undefined'
	        ? args[number]
	        : match
	      ;
	    });
	  };
	}

	var getData = (function() {
		$.get( 'get.geojson.js', function(data) {
			var dataStorage = data;
			console.log(dataStorage);
			geojsonLayer = L.geoJson(data, {
				onEachFeature: function(feature, layer) {
					var modalLink = modal.replace('{}', feature.properties.id)
					var rating_total = feature.properties.positive_ratings + feature.properties.negative_ratings
					console.log(rating_total)
					var rating = feature.properties.positive_ratings / rating_total;
					var popupString = "<p>{0}</p><p>{1}</p><p>{2}</p><div id='rate_bar'><div id='good_ratings'></div><div id='bad_ratings'></div></div>".format(
						feature.properties.location,
						feature.properties.building,
						rating)
					var popup = layer.bindPopup(popupString);
					popup.id = feature.properties.id;
				}
		    })
		    geojsonLayer.addTo(map);
		});
    });
    

	getData()

});
