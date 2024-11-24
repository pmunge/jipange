from django.urls import path
from .import views


urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('add_member', views.add_member, name='add_member'),
    path('add_contribution', views.add_contribution, name='add_contribution'),
    path('add_event',views.add_event, name="add_event"),
    path('member/<int:member_id>/contributions/', views.member_contributions, name='member_contributions')
]