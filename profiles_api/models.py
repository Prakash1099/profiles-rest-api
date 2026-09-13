from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
# THE ABOVE 3 DEFAULT MODELS ARE NEEDED TO MODIFY AND OVERRIDEE DJANGO'S
# DEFAULT USER MODELcd

from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for User Profiels"""

    """this will have some functions that will be used to manipulate 
    some of the objects within the UserProfile model class
    """

    def create_user(self, email, name, password=None):
        """Create a new User Profile"""

        if not email:
            raise ValueError("User must have an email address")

        # email = ''.join(email.split('@')[1].lower())

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)  # To save the password by encrypting it. hashing it. 
        user.save(using=self._db) ## Thi is standard to save an object in db to mention the db name

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user with given details"""
        
        user = self.create_user(email, name, password)

        # this is not defined in the userProfile class but still mentioned because these are coming form the PermissionsMixin
        user.is_superuser = True   
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in system"""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # if True user has Admin access

    #Model Manager - To use this custom user model in the django CL Tools.
    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #To use email and password insted of username and pwd
    REQUIRED_FIELDS = ['name']  #this has to be a list

    def get_full_name(self):
        """Retreive full name of the User"""
        return self.name

    def get_short_name(self):
        """Retreive short name of the User"""
        return self.name

    def __str__(self):
        """Return string representation of the user"""
        return self.email 


class ProfileFeedItem(models.Model):
    """Profile status update """

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text

    