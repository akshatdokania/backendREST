from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from userdata.api import UserInput, UserDetail
from account.api import UserCreate, UserLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/userdata/', UserInput.as_view(), name='userinput'),               #new patient
    path('api/userdata/<slug:id>', UserDetail.as_view(), name='userdetail'),    #when existing selected
    path('api/usercreate/', UserCreate.as_view(), name='usercreate'),           #registration
    path('api/userlogin/', UserLogin.as_view(), name='userlogin')                #userlogin 
]
