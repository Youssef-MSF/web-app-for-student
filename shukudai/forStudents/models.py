from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    preview = models.CharField(max_length=200, null=True)
    nb_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    commenter = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=4000)
    date_comment = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.comment


class Reminder(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
