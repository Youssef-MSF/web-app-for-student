from django.contrib import admin
from .models import Post, Comment, Reminder, Task

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reminder)
admin.site.register(Task)
