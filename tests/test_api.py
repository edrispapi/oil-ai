# tests/test_api.py
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class SensorQueryAPITest(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='u', password='p')
        self.client.login(username='u', password='p')
    def test_sensor_query(self):
        url = reverse('sensor_query')
        resp = self.client.post(url, {'question': 'علت افت فشار چاه x؟'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn('answer', resp.data)
