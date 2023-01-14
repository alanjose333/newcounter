from .views import RegisterAPI,LoginAPI,SignInAPI,SignUpAPI

from django.urls import path
from .import views
from knox import views as knox_views
urlpatterns = [
path('register',RegisterAPI.as_view(), name="register"),
path('login', LoginAPI.as_view(), name='login'),
path('logout', knox_views.LogoutView.as_view(), name='logout'),
path('api/auth/login', SignInAPI.as_view()),
path('api/auth/register', SignUpAPI.as_view()),
path('recordmeal/', views.RecordMeal.as_view()),
path('calory_status', views.calory_status, name="calory_status"),

path('food_store_by_user', views.food_store_by_user, name="food_store_by_user"),
path('activity_store_by_user', views.activity_store_by_user, name="activity_store_by_user"),

]