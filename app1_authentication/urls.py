from django.urls import path
from .views import Login, LogOut, UserList, UserCreation, UserStateChange, Update_user, UserPermissionAdd, UserPasswordChange
app_name = 'app1_authentication'
urlpatterns = [
    path('login',Login.as_view(),name="login"),
    path('logout',LogOut.as_view(),name="logout"),

    path('user_manage/user_list',UserList.as_view(),name="user_list"),
    path('user_manage/create_user',UserCreation.as_view(),name="create_user"),
    path('user_manager/user_state_chage/<str:u_id>/<str:state>/',UserStateChange.as_view(),name="user_state_chage"),
    path('user_manager/update_user',Update_user.as_view(),name="update_user"),
    path('user_manager/password_change/<str:u_id>',UserPasswordChange.as_view(),name="password_change"),
    path('user_manager/user_permission_add/<str:u_id>',UserPermissionAdd.as_view(),name="user_permission_add"),
]