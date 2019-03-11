from django.urls import path
from .views import RestaurantListView, RestaurantDetailView,\
    RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView,\
    MyPostView

urlpatterns = [
    path('', RestaurantListView.as_view(), name='home'),
    path('create/', RestaurantCreateView.as_view(), name='create'),
    path('<slug:slug>/', RestaurantDetailView.as_view(), name='detail'),
    path('<slug:slug>/update', RestaurantUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete', RestaurantDeleteView.as_view(), name='delete'),
    path('dashboard/myposts/', MyPostView.as_view(), name='my_posts'),
]
