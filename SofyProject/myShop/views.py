from django.shortcuts import render, redirect
from model

# Create your views here.

# Index view
class Index(View):
    def post(self, request):
        pass

    def get(self, request):
        pass


# Shop view
def shop(request):
    pass


# Login view
class Login(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# Logout view
def logout(request):
    pass


# Sign up view
class Signup(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

    def validateCustomer(self, customer):
        pass


# Cart view
class Cart(View):
    def get(self, request):
        pass


# Check out View
class CheckOut(View):
    def get(self, request):
        pass


# Order View
class OrderView(View):
    def get(self, request):
        pass