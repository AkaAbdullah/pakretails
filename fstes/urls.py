from django.contrib import admin
from django.urls import path
from login.views import home, loginuser,signupuser,profile,updateinfo
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('signup/',signupuser, name='signupuser'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('loginuser/',loginuser,name='loginuser'),
    path('profile/',profile,name='profile'),
    path('updateinfo/',updateinfo,name='updateinfo'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
