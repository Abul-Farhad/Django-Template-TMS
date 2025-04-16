from django.urls import path
# from .views import (
#     login_view,
#     logout_view,
#     register_view
# )

from .views import (
    LoginView,
    LogoutView, 
    RegisterView,
)

urlpatterns = [
    # path('login/', login_view, name='login'),
    # path('register/', register_view, name='register'),
    # path('logout/', logout_view, name='logout'),

    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]