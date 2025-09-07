from django.urls import path
# from . import views
from .views import ListingListCreateView, ListingDetailView
from .views import trigger_email


urlpatterns = [
    # path('listings/', views.HelloWorldView.as_view(), name='Hello-World-View'),
    path('', ListingListCreateView.as_view(), name='listing-list'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('send-email/', trigger_email, name='send-email'),

]