from django.http import response
from django.test import TestCase
from django.urls import reverse

class SnacksTest(TestCase):

    def test_base(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_base_template_base(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')

    def test_base_template_list(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

    """
    This test doesn't work. I was hoping that by running the server in one ubuntu window and testing in a second window I would be able to get out of the "chicken and egg" issue there, but it responded by saying that it did not use a template. I tried again checking for base.html and recieved the same response. When trying the third with and without a forward slash where marked I recieved an error saying that there was an unmatched open paren even though it was in fact matched with a closing paren.

    def test_base_template_detail(self):
        url = '127.0.0.1:8000/1'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_base_template_detail(self):
        url = '127.0.0.1:8000/1'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')

    def test_base_template_detail(self):
        url = f'{reverse('snack_list')}1'   <==== between '}' and '1'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
    """