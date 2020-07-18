import os
from datetime import date
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase

from .models import Maid

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
        self.assertEqual(maid.name, 'BBBBBBBBBBBBBBBBBBBBBBBB')
        self.assertEqual(maid.birthdate, date(1998, 4, 29))
        self.assertEqual(maid.description, 'Super Maid')
        self.assertEqual(maid.certificate, 'Best Maid 2012')
        self.assertEqual(maid.salary, 4000)

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
        self.assertEqual(maid.profile_image.name, 'profile.png')
        self.assertEqual(maid.name, 'BBBBBBBBBBBBBBBBBBBBBBBB')
        self.assertEqual(maid.birthdate, date(1998, 4, 29))
        self.assertEqual(maid.description, 'Super Maid')
        self.assertEqual(maid.certificate, 'Best Maid 2012')
        self.assertEqual(maid.salary, 4000)

        os.remove('profile.png')

