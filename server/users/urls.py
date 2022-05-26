from django.urls import path
from .views import BlacklistTokenView, CustomUserCreate, Username, UserProfileUpload, UpdateUser


app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist'),
    path('upload/', UserProfileUpload.as_view(), name='uploadimage'),
    path('username/', Username.as_view(), name='username'),
    path('username/<int:pk>/', UpdateUser.as_view(), name='updateuser'),
]
