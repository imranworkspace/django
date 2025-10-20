from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import StudentModel
# Create your tests here.

class StudentFunctionTestView(APITestCase):
    def setUp(self):
        self.student = StudentModel.objects.create(name="sonu",email="sonu@gmail.com",password="sonu123")
        self.list_url = reverse("api")
        self.details_url = reverse("api_details",args=[self.student.id])

    # for get - list
    def test_list(self):
        response = self.client.get(self.list_url)
        print("response",response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    # for post
    def test_post(self):
        json_data={
            "name":"zunnu",
            "email":"z@gmail.com",
            "password":"zunnu123"
        }
        response=self.client.post(self.list_url,data=json_data,format="json")
        print('response',response)
        self.assertEqual(response.data["name"],"zunnu")