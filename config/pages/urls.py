from .views import HomePageView, requestURL, AboutPageView, MySelfPageView
from django.urls import path


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('form/', requestURL, name="requestURL"),
    path('about/', AboutPageView.as_view(), name='about'),
    path('myself/', MySelfPageView.as_view(), name='myself'),
]