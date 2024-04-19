# urls.py
from django.urls import path
from .views import SignupView,DbViews,LoginView

urlpatterns = [
    
    path('signupApi/', SignupView.as_view(), name='api_token_auth'),
    path('dataApi/',DbViews.as_view(), name='database'),
    path('loginApi/',LoginView.as_view(), name='login'),

]
