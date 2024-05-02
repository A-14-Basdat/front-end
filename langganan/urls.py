from django.urls import path
from langganan.views import show_beli, show_langganan

app_name = 'langganan'

urlpatterns = [
    path('', show_langganan, name='show_langganan'),
    path('beli/', show_beli, name='show_beli'),
]