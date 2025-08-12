from django.urls import path
from generate_jwt.views import token_obtain
from example.views import example

urlpatterns = [
    path("api/token/", token_obtain, name="token_obtain"),
    path("api/example/", example, name="example"),
    
]
