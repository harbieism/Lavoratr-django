$(document).ready(function() {
    
    var youIcon = L.icon({
        iconUrl: '/static/lavoratr/img/peeman.png',
        iconSize: [20, 40],
        iconAnchor: [10, 20],
        popupAnchor: [0, 0]
    });
    var toiletIcon = L.icon({
        iconUrl: '/static/lavoratr/img/Toilet.png',
        iconSize: [40, 40],
        iconAnchor: [20, 20],
        popupAnchor: [0, -20]
    });
    var fToiletIcon = L.icon({
        iconUrl: '/static/lavoratr/img/Toilet_F.png',
        iconSize: [40, 40],
        iconAnchor: [20, 20],
        popupAnchor: [0, -20]
    });
    var mToiletIcon = L.icon({
        iconUrl: '/static/lavoratr/img/Toilet_M.png',
        iconSize: [40, 40],
        iconAnchor: [20, 20],
        popupAnchor: [0, -20]
    });
    
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
					if (rating_total == 0) {
						var goodWidth = 0;
						var rating = 0;
					} else {
						var rating = feature.properties.positive_ratings / rating_total;
						var goodWidth = rating * 100;
					}
					var popupString = "<p>{0}</p><p>{1}</p><p>{2}</p><div class='progress'><div class='progress-bar' role='progressbar' aria-valuenow='{3}' aria-valuemin='0' aria-valuemax='100' style='width: {3}%;'><span class='sr-only'>{3}%</span></div></div>".format(
						feature.properties.location,
						feature.properties.building,
						rating,
						goodWidth)
					var popup = layer.bindPopup(popupString);
					popup.id = feature.properties.id;
				}
		    })
		    geojsonLayer.addTo(map);
		});
    });
    

    map.on('popupopen', function(e) {

    });
	getData()

});
