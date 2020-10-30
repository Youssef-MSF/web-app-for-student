from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .models import Post, Comment, Reminder
from accounts.models import Student


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    reminders = Reminder.objects.all()
    return render(request, 'dashboard.html', {'reminders': reminders})


def forum(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'forum.html', {'posts': posts})


def add_new_post(request):
    return render(request, 'addPost.html')


def addPostTreatment(request):
    if request.method == 'POST':
        title = request.POST['title']
        preview = request.POST['preview']
        content = request.POST['content']

        student_email = request.POST['user_email']
        student = Student.objects.filter(email=student_email)[0]

        post = Post.objects.create(author=student, title=title, content=content, preview=preview)
        post.save()
        return redirect('/forum')

    else:
        return render(request, 'addPost.html')


def post_detail(request, post_title):
    post = get_object_or_404(Post, title=post_title)
    comments = Comment.objects.filter(post=post)
    return render(request, 'postDetail.html', {'post': post, 'comments': comments})


def send_comment(request):
    if request.method == 'POST':
        comment_content = request.POST['comment']
        commenter_email = request.POST['commenter_email']
        post_id = request.POST['post_id']
        commenter = Student.objects.filter(email=commenter_email)[0]
        post = Post.objects.filter(id=post_id)[0]

        comment = Comment.objects.create(comment=comment_content, commenter=commenter, post=post)
        comment.save()
        post.nb_comments += 1
        post.save()
        return redirect('/forum/post/' + post.title)
    else:
        return render(request, 'postDetail.html')


def upload_profile_image(request):
    if request.method == 'POST':
        uploaded_profile_image = request.POST['uploaded_profile_image']


def settings(request):
    return render(request, 'settings.html')


def update_profile(request):
    if request.method == 'POST':
        profile_pic = request.POST['profile_image']
        fullname = request.POST['fullname']
        age = request.POST['age']
        nationality = request.POST['nationality']
        user_id = request.POST['user_id']

        student = Student.objects.filter(id=user_id)[0]
        student.nationality = nationality
        student.age = age
        student.fullname = fullname
        student.image = profile_pic

        student.save()

        return redirect('/dashboard')

    else:
        return render(request, 'settings.html')


def set_reminder(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        reminder_title = request.POST['reminder_title']
        reminder_date = request.POST['reminder_date']

        student = Student.objects.filter(id=user_id)[0]
        reminder = Reminder.objects.create(title=reminder_title, date=reminder_date, student=student)

        reminder.save()

        return redirect('/dashboard')

    else:
        return render(request, 'dashboard.html')