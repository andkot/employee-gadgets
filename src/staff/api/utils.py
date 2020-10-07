# from django.contrib.auth import authenticate
# from rest_framework import serializers
# from ..models import Employee
#
#
# # def auth_employee(username, password):
# #     """ Authenticate a user based on email address as the user name. """
# #     try:
# #         user = Employee.objects.get(email=username)
# #         if user.check_password(password):
# #             return user
# #     except Employee.DoesNotExist:
# #         return None
#
#
# def get_and_auth_employee(email, password):
#     print(email, password)
#     employee = authenticate(username=email, password=password)
#     if employee is None:
#         raise serializers.ValidationError("Invalid username/password. Please try again!")
#     return employee
