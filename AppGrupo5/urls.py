from django.urls import path

from AppGrupo5 import views

urlpatterns = [
    
    path('instrumentos',views.instrumentos, name="instrumentos"),
    path('pedal', views.pedal, name= "pedal"),
    path('disco',views.disco, name= "disco"),
    path('', views.inicio, name="inicio"),
    path('cargainstrumento',views.Carga_Instrumento,name="cargainstrumento"),
    path('buscarinstrumento/',views.buscarinstrumento)
]

