from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
   path('dummy',views.dummy,name='dummy'),
#    path('booking',views.booking,name='booking'),

]
