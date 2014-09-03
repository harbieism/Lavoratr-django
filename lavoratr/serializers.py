from rest_framework_gis.serializers import GeoFeatureModelSerializer
from lavoratr.models import Toilet


class ToiletSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Toilet
        geo_field = "point"
        id_field = False
        fields = (
            'id', 'location', 'building', 'positive_ratings',
            'negative_ratings', 'gender', 'created',
            'single_occupancy', 'accesible', 'station',
            'times_authenticated',
        )
