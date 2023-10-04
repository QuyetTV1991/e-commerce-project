from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Products, Category, Customer, Order
from django.views.generic import View

# Create your views here.

# Index view
class Index(View):
    def post(self, request):
        pass

    def get(self, request):
        return HttpResponseRedirect(f'/shop{request.get_full_path()[1:]}')


# Shop view
def shop(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    
    products = None

    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_product_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    
    return render(request, 'index.html', data)


# Login view
class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('homepage')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'login.html', {'error': error_message})


# Logout view
def logout(request):
    request.session.clear()
    return redirect('login')


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
        return render(request, 'cart.html')


# Check out View
class CheckOut(View):
    def get(self, request):
        pass


# Order View
class OrderView(View):
    def get(self, request):
        pass