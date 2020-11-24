import random
from http.client import HTTPResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .models import Post, Comment, Reminder, Task, Book, Classroom, ClassroomMessage, Option, Poll
from accounts.models import Student

from PyDictionary import PyDictionary


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    reminders = Reminder.objects.all()

    tasks = Task.objects.all()

    return render(request, 'dashboard.html', {'reminders': reminders, 'tasks': tasks})


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
        fullname = request.POST['fullname']
        age = request.POST['age']
        nationality = request.POST['nationality']
        user_id = request.POST['user_id']

        student = Student.objects.filter(id=user_id)[0]

        profile_pic = request.FILES.get('profile_image', student.image.name)

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


def add_task(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        reminder_title = request.POST['task_title']
        reminder_date = request.POST['task_date']

        student = Student.objects.filter(id=user_id)[0]
        task = Task.objects.create(title=reminder_title, date=reminder_date, student=student)

        task.save()

        return redirect('/dashboard')

    else:
        return render(request, 'dashboard.html')


def translate(request):
    global description
    if request.method == 'POST':
        word = request.POST['word_to_search']

        translation = PyDictionary(word)
        description = translation.getMeanings()

    return render(request, 'dashboard.html', {'description': description})


def del_reminder(request):
    reminder_id = request.GET['id']
    Reminder.objects.filter(id=reminder_id).delete()
    return redirect('/dashboard')


def del_task(request):
    task_id = request.GET['id']
    Task.objects.filter(id=task_id).delete()
    return redirect('/dashboard')


def done_task(request):
    task_id = request.GET['id']
    task = Task.objects.filter(id=task_id)[0]
    task.is_done = True
    task.save()
    return redirect('/dashboard')


def revise(request):
    return render(request, 'revise.html')


def mybooks(request):
    books = Book.objects.all()

    return render(request, 'mybooks.html', {'books': books})


def add_new_book(request):
    if request.method == 'POST':
        book_title = request.POST['book_title']
        book = request.FILES.get('book')
        student_id = request.POST['user_id']

        student = Student.objects.filter(id=student_id)[0]

        new_book = Book.objects.create(title=book_title, book=book, student=student)

        new_book.save()

        return redirect('/myBooks')

    return render(request, 'addBook.html')


def classroom_dashboard(request):
    if request.method == 'POST':
        classroom_id = request.POST['classroom_id']
        user_id = request.POST['user_id']

        user = Student.objects.filter(id=user_id)[0]
        classroom = Classroom.objects.filter(id_classroom=classroom_id)[0]

        classroom.users.add(user)

        classroom.save()
        return redirect('/classroom/' + classroom_id)
    else:
        return render(request, 'classroom_dashboard.html')


def send_classroom_message(request):
    if request.method == 'POST':
        message_content = request.POST['message_to_discussion']
        writer_id = request.POST['user_id']
        classroom_id = request.POST['classroom_id']
        writer = Student.objects.filter(id=writer_id)[0]
        classroom = Classroom.objects.filter(id_classroom=classroom_id)[0]

        message = ClassroomMessage.objects.create(message_content=message_content, writer=writer, classroom=classroom)

        message.save()

        return redirect('/classroom/' + classroom_id)


def classroom_detail(request, classroom_id):
    classroom = get_object_or_404(Classroom, id_classroom=classroom_id)
    classroom_corr = Classroom.objects.filter(id_classroom=classroom_id)[0]
    messages = ClassroomMessage.objects.all()
    try:
        poll = Poll.objects.filter(classroom=classroom_corr)[0]
    except:
        poll = None
    return render(request, 'classroom.html', {'classroom_corr': classroom_corr, 'messages': messages, 'poll': poll})


def create_classroom(request):
    letters_nums = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                    'P',
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '_']

    host_id = request.POST['host_id']
    host = Student.objects.filter(id=host_id)[0]

    all_classroom_ids = []

    all_classrooms = Classroom.objects.all()
    for classroom in all_classrooms:
        all_classroom_ids.append(classroom.id_classroom)

    random_classroom_id = ''
    for i in range(random.randint(6, 15)):
        random_classroom_id += random.choice(letters_nums)

    if random_classroom_id in all_classroom_ids:
        create_classroom(request)
    else:
        classroom = Classroom.objects.create(id_classroom=random_classroom_id, host_id=host_id)
        classroom.users.add(host)
        classroom.save()
        return redirect('/classroom/' + random_classroom_id)


def create_poll(request):
    user_id = request.POST['user_id']
    classroom_id = request.POST['classroom_id']
    poll_title = request.POST['poll_title']

    creator = Student.objects.filter(id=user_id)[0]
    classroom = Classroom.objects.filter(id_classroom=classroom_id)[0]

    poll = Poll.objects.create(title=poll_title, creator=creator, classroom=classroom)
    poll.save()
    options = []
    for parameter in request.POST:
        if 'Option' not in parameter:
            continue
        else:
            options.append(parameter)
            option = Option.objects.create(value=request.POST[parameter], poll_id=poll.id)
            option.save()

            poll.options.add(option)
            poll.save()

    classroom.has_poll = 1
    classroom.save()

    return redirect('/classroom/' + classroom_id)
