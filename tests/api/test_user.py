from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class CategoryTests(APITestCase):
  client = APIClient()

  def test_create_create(self):

    url = '/api/v1/users/'
    data = {"phone_number":"0905116362","password":"Nguyen123@"}
    response = self.client.post(url, data, format='json')
    assert response.status_code == 403