from django.urls import path
from . import views
from results import views as resview

urlpatterns = [

    #User Client
    path('', views.home, name="home"),
    path('logout/',views.log_out, name="logout"),
    path('login/', views.log_in, name="login"),
    path('register/', views.register, name="register"),
    path('details/<int:qid>', views.details, name='details'),
    path('view_test/<str:test_type>', views.view_tests, name='view_tests'),

    #Test
    path('test/start/<int:tid>', views.start_test,  name="start_test"),
    
 
]
