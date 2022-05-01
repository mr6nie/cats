from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.CatsView.as_view(), name="cats_list"),
    path('create/', views.CatCreateView.as_view(), name="create_cat"),
    path('<uuid:uuid>/', views.SingleCatView.as_view({'get': 'retrieve'}), name="single_cat"),
    path('<uuid:uuid>/update/', views.SingleCatView.as_view({'put': 'update'}), name="update_cat"),
    path('<uuid:uuid>/delete/', views.SingleCatView.as_view({'post': 'destroy'}), name="delete_cat"),
]
