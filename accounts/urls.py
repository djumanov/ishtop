from django.urls import path
from .views import CreateAccountView, ConfirmAccountView

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='create-account'),
    path('confirm-account/', ConfirmAccountView.as_view(), name='confirm-account'),
]
