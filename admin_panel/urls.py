from django.urls import path
from . import views

urlpatterns = [
    #Admin Panel
    path('', views.admin_panel, name="dashboard"),
    path('manage/practice/', views.manage_practice, name="mprac"),
    path('manage/grand/', views.manage_grand, name="mgrand"),
    path('manage/all/', views.list_all_tests, name="list_all"),
    path('manage/<int:tid>', views.test_view, name='test_view'),
    path('manage/add/<int:tid>', views.add_question, name="add_question"),
    path('manage/delete/question/<int:tid>/<int:quid>', views.delete_question, name="delete_question"),
    path('manage/create/', views.create_test, name='create_test'),
    path('manage/delete/test/<int:tid>', views.delete_test, name="delete_test"),
]
