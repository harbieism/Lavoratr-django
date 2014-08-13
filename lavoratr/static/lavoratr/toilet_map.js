var southWest = new L.LatLng(-85.0, -180.0);
var northEast = new L.LatLng(85.0, 180.0);
var restrictBounds = new L.LatLngBounds(southWest, northEast);

var mapOptions = {
    maxBounds: restrictBounds
};


var map = L.map('map', mapOptions);
map.options.minZoom = 3;


mapLink =
    '<a href="http://openstreetmap.org">OpenStreetMap</a>';
L.tileLayer(
        'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; ' + mapLink,
            maxZoom: 17,
        })
    .addTo(map);


L.geoJson($data, {
    onEachFeature: onEachFeature
}).addTo(map);


map.on('locationfound', onLocationFound);
map.locate({setView: true, maxZoom: 17});


function onEachFeature(feature, layer) {
    if (feature.properties) {
        var popupString = '<div class="popup">';
        popupString += 'Location: ' + feature.properties.location + '<br />';
        popupString += 'Building: ' + feature.properties.building + '<br />';
        realRating = feature.properties.rating / feature.properties.times_rated;
        popupString += 'Rating: ' + realRating + '<br />';
        popupString += 'Gender: ' + feature.properties.gender + '<br />';
        link = ('<a href=/lavoratr/detail/' + feature.properties.id + '/ >detail</a>');
        popupString += link + '</div>';
        layer.bindPopup(popupString);
    };

    var hoverStyle = {
        color: '#2262CC', 
        weight: 3,
        opacity: 0.6,
        fillOpacity: 0.65,
        fillColor: '#2262CC'
    };

    var style = {
        color: "#2262CC",
        weight: 2,
        opacity: 0.6,
        fillOpacity: 0.1,
        fillColor: "#2262CC"
    };

    if (!(layer instanceof L.Point)) {
        layer.on('mouseover', function () {
            layer.setStyle(hoverStyle);
        });
        layer.on('mouseout', function () {
            layer.setStyle(style);
        });
    }
};
    

function onLocationFound(e) {
    var radius = e.accuracy / 2;
    var lat = e.latlng.lat;
    var lng = e.latlng.lng;
    $('#lat').val(parseFloat(lat.toString()));
    $('#lng').val(parseFloat(lng.toString()));



    var userMarker = L.marker(e.latlng, {draggable: true}).addTo(map)
        .bindPopup(lat.toString()).openPopup();
    
    L.circle(e.latlng, radius).addTo(map);

    userMarker.on('dragend', function(e){
        var coords = e.target.getLatLng();
        lat = coords.lat;
        lng = coords.lng;
        $('#lat').val(parseFloat(lat.toString()));
        $('#lng').val(parseFloat(lng.toString()));


    });

    $('#add_toilet').click(function (event) {
        window.location="add_toilet/" + lat + "/" + lng + "/";
    });
}