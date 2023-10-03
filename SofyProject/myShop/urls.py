from django.urls import path
from . import views
from './middlewares' import auth

urlpatterns = [
    path("", views.Index.as_view(), name="homepage"),
    path("shop", views.shop, name="shop"),
    path("signup", views.Signup.as_view(), name="signup"),
    path("login", views.Login.as_view(), name="login"),
    path("logout", views.logout, name="logout"),
    path("cart", auth.auth_middleware(Cart.as_views()), name="cart"),
    path("check-out", CheckOut.as_view(), name="checkout"),
    path("orders", auth.auth_middleware(OrderView.as_view()), name="orders"),
]
