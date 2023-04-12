from django.urls import path
from apps.views import CustomLoginView, RegisterView, IndexView

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('', CustomLoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register')
]
