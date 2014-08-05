var map = L.map('map');
mapLink =
    '<a href="http://openstreetmap.org">OpenStreetMap</a>';
L.tileLayer(
        'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; ' + mapLink,
            maxZoom: 18,
        })
    .addTo(map);

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
map.on('locationfound', onLocationFound);
map.locate({setView: true, maxZoom: 16});


function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    var link = ('<a href=/lavoratr/detail/' + feature.properties.id + '/ >detail</a>');
    layer.bindPopup(link);
}

L.geoJson($data, {
        onEachFeature: onEachFeature
    })
    .addTo(map);