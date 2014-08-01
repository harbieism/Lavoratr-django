var map = L.map('map');
function onLocationFound(e) {
    var radius = e.accuracy / 2;

    L.marker(e.latlng).addTo(map)
        .bindPopup("You are within " + radius + " meters from this point").openPopup();

    L.circle(e.latlng, radius).addTo(map);
}
map.on('locationfound', onLocationFound);
map.locate({setView: true, maxZoom: 16});
mapLink =
    '<a href="http://openstreetmap.org">OpenStreetMap</a>';
L.tileLayer(
        'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; ' + mapLink,
            maxZoom: 18,
        })
    .addTo(map);


function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    var link = ('<a href=/lavoratr/detail/' + feature.properties.id + '/ >detail</a>');
    layer.bindPopup(link);
}

L.geoJson($data, {
        onEachFeature: onEachFeature
    })
    .addTo(map);