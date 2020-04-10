from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.utils import timezone
import os
# Create your models here.
class MedicoManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser,
                           date_joined=now, **extra_fields)
        user.set_password(password)
        return user

    def create_user(self, email, password, **extra_fields):
        user = self._create_user(email, password, is_staff=False, is_superuser=False, **extra_fields)
        #permissions
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user

class Medico(AbstractBaseUser, PermissionsMixin):
    OCCUPATION_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Resident', 'Resident'),
        ('Teacher', 'Teacher')
    ]

    crm = models.CharField(unique=True, max_length=15, null=True)
    email = models.EmailField(unique=True, max_length=60)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    occupation = models.CharField(max_length=10, choices=OCCUPATION_CHOICES, blank=False, null=True)

    is_staff = models.BooleanField('staff_status', default=False)#Pode se logar como admin
    is_active = models.BooleanField('user_active', default=True)
    is_trusty = models.BooleanField('trusty', default=False)#Diz se o usuário confirmou a conta


    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MedicoManager()

    def get_upload_handler(instance, filename):
        email = instance.email
        return os.path.join('static', 'medicos', email, filename)

    avatar = models.ImageField(upload_to=get_upload_handler, null=True)


    def __str__(self):
        return self.first_name + " " +self.last_name
