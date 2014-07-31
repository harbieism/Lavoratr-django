var map = L.map('map')
    .setView([-41.2858, 174.78682], 14);
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