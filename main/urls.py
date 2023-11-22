from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('daniel/<int:pk>', views.show_more_for_daniel, name='details_daniel'),
    path('rex/<int:pk>', views.show_more_for_rex, name='details_rex'),
    path('samantha/<int:pk>', views.show_more_for_samantha, name='details_samantha')
]