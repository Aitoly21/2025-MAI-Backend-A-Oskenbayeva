from django.urls import path
from core import views

urlpatterns = [
    # Profile
    path('profile/', views.profile_list_view),
    path('profile/create', views.profile_create_view),
    path('profile/search/', views.profile_search_view),

    # Course
    path('course/', views.course_list_view),
    path('course/create', views.course_create_view),
    path('course/search/', views.course_search_view),

    # Category
    path('category/', views.category_list_view),
    path('category/create', views.category_create_view),
    path('category/search/', views.category_search_view),
]
