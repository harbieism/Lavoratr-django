var southWest = new L.LatLng(-85.0, -180.0);
var northEast = new L.LatLng(85.0, 180.0);
var restrictBounds = new L.LatLngBounds(southWest, northEast);

var mapOptions = {
    maxBounds: restrictBounds
};


var youIcon = L.icon({
    iconUrl: '/static/lavoratr/img/peeman.png',
    iconSize:     [20, 40], // size of the icon
    iconAnchor:   [10, 20], // point of the icon which will correspond to marker's location
    popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});

var toiletIcon = L.icon({
    iconUrl: '/static/lavoratr/img/Toilet.png',
    iconSize:     [40, 40], // size of the icon
    iconAnchor:   [20, 20], // point of the icon which will correspond to marker's location
    popupAnchor:  [0, -20] // point from which the popup should open relative to the iconAnchor
});

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
    onEachFeature: onEachFeature,
    pointToLayer: function (feature, latlng) {
        return L.marker(latlng, {icon: toiletIcon, riseOnHover: true});
    }
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
        link = (
            "<div class='detail_link'><a href=/lavoratr/detail/"
            + feature.properties.id + "/>detail</a></div>"
        );
        popupString += link + '</div>';
        layer.bindPopup(popupString);
        layer.icon = toiletIcon;
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
        });
        layer.on('mouseout', function () {
        });
    }
};
    

function onLocationFound(e) {
    var radius = e.accuracy / 2;
    var lat = e.latlng.lat;
    var lng = e.latlng.lng;
    $('#lat').val(parseFloat(lat.toString()));
    $('#lng').val(parseFloat(lng.toString()));



    var userMarker = L.marker(e.latlng, {icon: youIcon, draggable: true}).addTo(map);
    
    L.circle(e.latlng, radius).addTo(map);

    userMarker.on('dragend', function(e){
        var coords = e.target.getLatLng();
        lat = coords.lat;
        lng = coords.lng;
        $('#lat').val(parseFloat(lat.toString()));
        $('#lng').val(parseFloat(lng.toString()));


    });

    $('#add_restroom').click(function (event) {
        window.location="add_toilet/" + lat + "/" + lng + "/";
    });
}