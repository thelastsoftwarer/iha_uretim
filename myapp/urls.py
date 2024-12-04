# myapp/urls.py
from django.urls import path
from .views import register, user_login, user_logout

from . import views
from .views import (
    AircraftListView, AircraftCreateView, AircraftUpdateView, 
    AircraftDeleteView, AircraftDetailView
)

urlpatterns = [
    path('parts/', views.PartListView.as_view(), name='part-list'),
     path('', AircraftListView.as_view(), name='aircraft-list'),
    path('create/', AircraftCreateView.as_view(), name='aircraft-create'),
    path('<int:pk>/update/', AircraftUpdateView.as_view(), name='aircraft-update'),
    path('<int:pk>/delete/', AircraftDeleteView.as_view(), name='aircraft-delete'),
    path('<int:pk>/', AircraftDetailView.as_view(), name='aircraft-detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]
