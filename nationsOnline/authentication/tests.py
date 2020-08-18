import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from authentication.models import User
from authentication.serializers import UserSerializer

client = Client()
CONTENT_TYPE = 'application/json'

class CreateUserTest(TestCase):
    def setUp(self):        
        self.userData = json.dumps({
            'username': 'testUser',
            'password': 'testPassword',
        })
    
    def test_create_user(self):
        response = client.post(reverse('create-user'), self.userData, CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, 'POST returns no errors')