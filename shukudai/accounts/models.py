from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class StudentManager(BaseUserManager):
    def create_user(self, email, username, fullname, gender, age, nationality, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(email=self.normalize_email(email), username=username, fullname=fullname, gender=gender,
                          age=age, nationality=nationality
                          , )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, fullname, gender, age, password=None):
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            fullname=fullname,
            gender=gender,
            age=age,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Student(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    fullname = models.CharField(max_length=40)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=60, unique=True)
    nationality = models.CharField(max_length=100, default=' ')
    image = models.ImageField(upload_to='pics')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'fullname', 'gender', 'age']

    objects = StudentManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
