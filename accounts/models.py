from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):    
    """
    CustomUser model extends the default AbstractUser model.

        This model introduces different user types:
        - Admin (1)
        - Guest (2)
        - Faculty (3)
        - Student (4)
        
        Each user will have a user type associated with them, which helps in assigning roles 
        and permissions across the service desk system.
    """

    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('guest', 'Guest'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    verification_status = models.CharField(max_length=20, default='unverified')
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    """
    UserProfile model extends the default models.Model.

        This model introduces additional fields for each user type:
        - id_number: Only for students
        - department: Only for faculty
        - affiliated_organization: Only for guests
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=30, blank=True, null=True)  # Only for students
    department = models.CharField(max_length=100, blank=True, null=True)  # Only for faculty
    affiliated_organization = models.CharField(max_length=100, blank=True, null=True)  # Only for guests

    def __str__(self):
        return f"{self.user.user_type.capitalize()} Profile: {self.user.username}"
