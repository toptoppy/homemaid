from django.test import TestCase
from datetime import date

from ..models import Maid
from ..serializers import MaidSerializer

class TestMaidSerializer(TestCase):
    def test_serializer_should_serializer_object_to_json(self):
        # Given
        Maid.objects.create(
            name='BBBBBBBBBBBBBBBBBBBBBBBB',
            birthdate=date(1998, 4, 29),
            description='Super Maid',
            certificate='Best Maid 2012',
            salary=4000
        )
        Maid.objects.create(
            name='CCCCCCCCCCCCCCCCCCCCCCCC',
            birthdate=date(1998, 4, 23),
            description='Ultra Maid',
            certificate='Best Maid 2020',
            salary=4000000
        )

        # When
        maid = Maid.objects.all()
        serializer = MaidSerializer(maid, many=True)

        # Then
        assert serializer.data == [{'id': 1 ,'name': 'BBBBBBBBBBBBBBBBBBBBBBBB',}, {'id': 2 ,'name': 'CCCCCCCCCCCCCCCCCCCCCCCC'}]
