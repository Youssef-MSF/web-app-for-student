from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('forum/', views.forum, name='forum'),
    path('forum/post/<str:post_title>/', views.post_detail, name='post_detail'),
    path('add+new+post/', views.add_new_post, name='addNewPost'),
    path('addPostTreatment/', views.addPostTreatment, name='addPostTreatment'),
    path('comment', views.send_comment, name='comment'),
    path('upload_profile_image', views.upload_profile_image, name='upload_profile_image'),
    path('settings/', views.settings, name='settings'),
    path('settings/update_profile', views.update_profile, name='update_profile'),
    path('reminder/', views.set_reminder, name='set_reminder')
]
