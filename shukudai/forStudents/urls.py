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
    path('reminder/', views.set_reminder, name='set_reminder'),
    path('add_task/', views.add_task, name='add_task'),
    path('dictionary/', views.translate, name='dictionary'),
    path('del_reminder/', views.del_reminder, name='del_reminder'),
    path('del_task/', views.del_task, name='del_task'),
    path('done_task/', views.done_task, name='done_task'),
    path('revise/', views.revise, name='revise'),
    path('myBooks/', views.mybooks, name='mybooks'),
    path('add_book/', views.add_new_book, name='addBook'),
    path('classroom_dashboard/', views.classroom_dashboard, name='classroom_dashboard'),
    path('send_message_classroom/', views.send_classroom_message, name='send_classroom_message'),
    path('classroom/<str:classroom_id>/', views.classroom_detail, name='classroom_detail'),
    path('create_classroom/', views.create_classroom, name='create_classroom'),
    path('create_poll/', views.create_poll, name='create_poll')
]
