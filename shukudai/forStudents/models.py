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


class Task(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    book = models.FileField(upload_to='books')
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.book.url


class Classroom(models.Model):
    id_classroom = models.CharField(max_length=100)
    host_id = models.IntegerField(default=0)
    users = models.ManyToManyField('accounts.Student')
    has_poll = models.IntegerField(default=0)

    def __str__(self):
        return self.id_classroom


class ClassroomMessage(models.Model):
    message_content = models.CharField(max_length=100)
    writer = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, null=True)
    classroom = models.ForeignKey(Classroom, null=True, on_delete=models.SET_NULL)
    sent_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.message_content


class Option(models.Model):
    value = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    poll_id = models.CharField(max_length=20)

    def __str__(self):
        return self.value


class Poll(models.Model):
    title = models.CharField(max_length=100)
    options = models.ManyToManyField(Option)
    creator = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
