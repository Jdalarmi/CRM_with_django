
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path("login/", views.login, name="login"),
    path("login/submit", views.submit_login, name="submit_login"),
    path("logout/", views.logout, name="logout"),
    path('customers/', include('customers.urls'))
]
