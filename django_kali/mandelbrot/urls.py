from django.urls import path
from . import views

urlpatterns = [
#    path("",views.home,name="home")
    path("plot_2/",views.plot_fao_2,name="plot_fao_2")
]
