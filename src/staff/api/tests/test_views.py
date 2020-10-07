from rest_framework.test import APITestCase
from rest_framework import status


class TestEmployeeViewUp(APITestCase):
    def test_registration_1(self):
        data = {
            "name": "a1a",
            "email": "a1aa@aaa.aaa",
            "position": "1",
            "avatar": None,
            "password": "123",
            "password2": "1123"
        }

        response = self.client.post("/api/v1/staff/employees/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_registration_2(self):
        data = {
            "name": "aaa",
            "email": "aaaa@aaa.aaa",
            "position": "1",
            "avatar": None,
            "password": "123",
            "password2": "123"
        }

        response = self.client.post("/api/v1/staff/employees/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_retrieve(self):
    #     request = APIRequestFactory().get("")
    #     emp_detail = CatViewSet.as_view({'get': 'retrieve'})
    #     cat = Cat.objects.create(name="bob")
    #     response = cat_detail(request, pk=cat.pk)
    #     self.assertEqual(response.status_code, 200)
    #
    #     response = self.client.get("/api/v1/staff/employees/1/")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)