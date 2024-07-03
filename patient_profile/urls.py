from django.urls import path
from .views import RegisterView, LoginView, LogoutView
# from .views import LoginView, RegisterView, UserView, LogoutView, ValidateView, GetUsernamesAPIView
from django.urls import path
from .views import PatientListCreateView, PatientRetrieveUpdateDestroyView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patient-detail'),
]