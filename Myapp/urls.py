# urls.py
from django.urls import path
from .views import SignupView,DbViews,LoginViews

urlpatterns = [
    
    path('signupApi/', SignupView.as_view(), name='api_token_auth'),
    path('dataApi/',DbViews.as_view(), name='database'),
    path('loginApi/',LoginViews.as_view(), name='login'),

]
