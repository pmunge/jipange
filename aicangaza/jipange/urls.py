from django.urls import path
from.import views


urlpatterns = [
    path('', views.contributionrecords, name='contributionrecords'),
    path('member_list', views.member_list, name='member_list'),
    path('event_list', views.event_list, name='event_list'),
    path('add_member', views.add_member, name='add_member'),
    path('add_contribution', views.add_contribution, name='add_contribution'),
    path('add_event',views.add_event, name="add_event"),
    path('member/<int:member_id>/contributions/', views.member_contributions, name='member_contributions'),
    path('register', views.register, name="register"),
    path('login', views.my_login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('event_contribution/<int:event_id>/event_contribution/', views.event_contribution, name='event_contribution'),
    path('member_contribution/<int:member_id>/member_contribution/', views.member_contribution, name='member_contribution'),
    #path('update/<int:pk>', views.update, name="update"),
]