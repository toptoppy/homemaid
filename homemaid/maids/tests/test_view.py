from datetime import date
from unittest.mock import patch

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


class TestMaidListAnotherView(TestCase):
    def test_view_should_respond_200(self):
        response = self.client.get(reverse('maid-another-list'))
        assert response.status_code == 200

    def test_view_should_display_maid_another_list(self):
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
        response = self.client.get(reverse('maid-another-list'))

        # Then
        assert '<li>BBBBBBBBBBBBBBBBBBBBBBBB</li>' in str(response.content)
        assert '<li>CCCCCCCCCCCCCCCCCCCCCCCC</li>' in str(response.content)


class TestMaidAddView(TestCase):
    def test_view_should_respond_200(self):
        response = self.client.get(reverse('maid-add'))
        assert response.status_code == 200

    def test_view_should_have_maid_form(self):
        response = self.client.get(reverse('maid-add'))

        assert '<form action="." method="POST">' in str(response.content)
        assert '<input type="hidden" name="csrfmiddlewaretoken" value=' in str(response.content)

        input_field = '<input type="text" name="name" maxlength="300" required id="id_name">'
        assert input_field in str(response.content)

        button_field = '<button class="btn btn-primary" type="submit">Submit</button>'
        assert button_field in str(response.content)

    def test_submit_form_should_save_new_maid(self):
        data = {
            'name': 'toptoppy'
        }
        self.client.post(reverse('maid-add'), data=data)

        maid = Maid.objects.last()

        assert maid.name == 'toptoppy'
    
    @patch('maids.views.send_mail')
    def test_after_submit_form_email_should_be_send(self, mock):
        data = {
            'name': 'toptoppy'
        }
        self.client.post(reverse('maid-add'), data=data)

        mock.assert_called_once_with('Subject here', 
                                     'Here is the message.', 
                                     'toptopy@odds.team', 
                                     ['toptopy@odds.team'], 
                                     fail_silently=False)