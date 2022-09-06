

from django.contrib import admin
from django.urls import path, include

from account import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add_user/', views.AddUserView.as_view(), name='add_user'),
    path('admin_app/', include('admin_app.urls')),
    path('employee_app/', include('employee_app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
