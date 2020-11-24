from django.contrib import admin
from .models import Post, Comment, Reminder, Task, Book, Classroom, ClassroomMessage, Option, Poll

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reminder)
admin.site.register(Task)
admin.site.register(Book)
admin.site.register(Classroom)
admin.site.register(ClassroomMessage)
admin.site.register(Option)
admin.site.register(Poll)
