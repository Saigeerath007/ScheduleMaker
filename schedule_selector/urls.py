from django.urls import path
from . import views
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("preference/", views.preference, name="preference"),
    # path('', ),
]
