import os
from datetime import date
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase

from ..models import Maid

class TestMaid(TestCase):
    def test_model_should_have_defined_fields(self):
        # Given
        Maid.objects.create(
            name='BBBBBBBBBBBBBBBBBBBBBBBB',
            birthdate=date(1998, 4, 29),
            description='Super Maid',
            certificate='Best Maid 2012',
            salary=4000
        )

        # When
        maid = Maid.objects.last()

        # Then
        assert maid.name == 'BBBBBBBBBBBBBBBBBBBBBBBB'
        assert maid.birthdate ==  date(1998 ,  4 ,  29)
        assert maid.description ==  'Super Maid'
        assert maid.certificate == 'Best Maid 2012'
        assert maid.salary == 4000

    def test_model_should_have_image_fields(self):
        # Given
        mock = MagicMock(spec=File)
        mock.name = 'profile.png'

        Maid.objects.create(
            profile_image=mock,
            name='BBBBBBBBBBBBBBBBBBBBBBBB',
            birthdate=date(1998, 4, 29),
            description='Super Maid',
            certificate='Best Maid 2012',
            salary=4000
        )

        # When
        maid = Maid.objects.last()

        # Then
        assert maid.profile_image.name == 'profile.png'

        os.remove('profile.png')

    def test_model_should_have_created_and_updated_fields(self):
        # Given
        Maid.objects.create(
            name='BBBBBBBBBBBBBBBBBBBBBBBB',
            birthdate=date(1998, 4, 29),
            description='Super Maid',
            certificate='Best Maid 2012',
            salary=4000
        )

        # When
        maid = Maid.objects.last()

        # Then
        assert maid.created is not None
        assert maid.modified is not None



