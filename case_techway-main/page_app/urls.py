from django.urls import path
from page_app.views import index, contato, services

urlpatterns = [
    # Cadastrar URLs aqui
    path('home/', index),
    path('contato/', contato),
    path('contato/', services)
]