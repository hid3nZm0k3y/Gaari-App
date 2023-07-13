"""
URL configuration for crud_form project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import settings
  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gaari.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('social-auth/', include('social_django.urls', namespace='social')),  
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if(settings.SOCIAL_AUTH_GITHUB_KEY):
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0, 
        path("accounts/login/", auth_views.LoginView.as_view(template_name=social_login)),                   
    )