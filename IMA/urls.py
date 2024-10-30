"""
URL configuration for IMA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from IMA import settings
from Pages import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.indexView, name="index"),
    path("about-us/", views.aboutView, name="about-us"),
    path("contact-us/", views.contactView, name="contact-us"),
    path("service/<slug:url_title>/", views.serviceView, name="service"),
    path("case/<slug:url_title>/", views.caseView, name="case"),
    path("team/<slug:url_title>/", views.teamView, name="team"),
    path("members/", views.teamMembersView, name="members"),
    path("post/<slug:url_title>", views.blogPostView, name="post"),
    path("blog/", views.blogView, name="blog"),
    path("cases/", views.casesView, name="cases"),
    path("privacy/", views.privacyView, name="privacy"),
    path("terms/", views.termsView, name="terms"),
    path("services/", views.servicesView, name="services"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
