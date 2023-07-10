from django.urls import path
from todo import views

app_name = "todo"

urlpatterns = [
    path('', views.ItemList.as_view(), name="list"),
    path('add/', views.ItemCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ItemUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.ItemDelete.as_view(), name='delete'),
    path(
        "check/<int:pk>/",
        views.ItemCheck.as_view(),
        name="check",
    ),
]
