"""django_kali URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include,path
from register import views as v_register
from plotlyplot import views as v_plotlyplot
from mandelbrot import views as v_mandelbrot

urlpatterns = [
    path("",include("lito_django.urls")),
    path("<int:id>",include("lito_django.urls")),
    path("home",include("lito_django.urls")),
    path("create/",include("lito_django.urls")),
    path("register/",v_register.register,name="register"),
    path('admin/', admin.site.urls),
    path("",include("django.contrib.auth.urls")),
    path("plot/",v_plotlyplot.plot_fao,name="plot_fao"),
    path("plot_2/",v_mandelbrot.plot_fao_2,name="plot_fao_2"),
]
