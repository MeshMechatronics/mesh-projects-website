from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Nullable ve boş olabilir
    start_date = models.DateField(null=True, blank=True)  # Nullable ve boş olabilir
    end_date = models.DateField(null=True, blank=True)  # Nullable ve boş olabilir
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Nullable ve boş olabilir
    tasks = models.TextField(blank=True, null=True)  # Nullable ve boş olabilir
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name


class Quote(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='quotes')

    def __str__(self):
        return f"{self.customer_name} - {self.product_name}"
    
class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Boş geçilebilmesini sağlayın
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='materials', default=1)

    def __str__(self):
        return self.name
    
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

