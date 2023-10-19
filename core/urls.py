from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path("", views.index,name="index"),
    path("agent_dashboard/", views.agent_dashboard, name="agent_dashboard"),
    path("agent_management/",  views.account_agency_management, name="agent_management"),
    path("about/",  views.about_us, name="about_us"),
    path("blog/",  views.blog, name="blog"),
    path("contact/",  views.contact_us, name="contact"),
    path("register", views.register_request, name="register"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]