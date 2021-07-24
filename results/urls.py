from django.urls import path
from . import views

urlpatterns = [
    path('', views.result, name="result"),
    path('<int:tid>', views.result_page, name="result_page"),
    path('<int:tid>/<int:rid>/report', views.report, name="report"),
]
