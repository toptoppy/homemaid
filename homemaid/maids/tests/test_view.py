from datetime import date

from django.test import TestCase
from django.urls import reverse

from ..models import Maid

class TestMaidListView(TestCase):
    def test_view_should_respond_200(self):
        response = self.client.get(reverse('maid-list'))
        assert response.status_code == 200
    
    def test_view_should_display_maid_list(self):
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
        response = self.client.get(reverse('maid-list'))

        # Then
        assert '<li>BBBBBBBBBBBBBBBBBBBBBBBB</li>' in str(response.content)
        assert '<li>CCCCCCCCCCCCCCCCCCCCCCCC</li>' in str(response.content)