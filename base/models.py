from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class CustomUser(AbstractUser):
    """
    Custom user model for representing users with additional fields.
    """

    # Types of users in this project
    EMPLOYEE = 'employee'
    ADMINISTRATOR = 'administrator'

    USER_TYPE_CHOICE = (
        (EMPLOYEE, 'Employee'),
        (ADMINISTRATOR, 'Administrator'),
    )

    # Name or username of the user
    username = models.CharField(max_length=200)
    # Employee or administrator
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICE, default=EMPLOYEE)
    # User's email address
    email = models.EmailField(unique=True)
    # Contact phone number
    phone_number = models.CharField(
        max_length=24, unique=True, null=True, blank=True)
    # Date of birth
    birthdate = models.DateField(null=True, blank=True)
    # Current address of the user
    address = models.CharField(max_length=255, null=True, blank=True)
    # User's profile picture
    profile_image = models.ImageField(null=True, default="avatar.svg")
    # Flag indicating account status
    is_active = models.BooleanField(default=False)
    # Many-to-Many relationship with Group model representing user groups.
    groups = models.ManyToManyField(
        Group,
        # Reverse relation name for accessing CustomUser instances from Group instances.
        related_name='customuser_set',
        blank=True,
        verbose_name='groups'
    )
    # Many-to-Many relationship with Permission model representing user-specific permissions.
    user_permissions = models.ManyToManyField(
        Permission,
        # Reverse relation name for accessing CustomUser instances from Permission instances.
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        """ Class Meta for ordering user objects """

        ordering = ['username']

    def __str__(self):
        return str(self.username)


class Restaurant(models.Model):
    """ Restaurant model with appropriate fields need to represent the restaurant onject """

    # Name or title of the restaurant
    restaurant_name = models.CharField(max_length=255, unique=True)
    # ID of the managing administrator
    managing_admin = models.ForeignKey(
        CustomUser,
        related_name='restaurant',
        null=True,
        on_delete=models.SET_NULL,
    )
    # Brief summary of the restaurant
    description = models.TextField(null=True, blank=True)
    # Physical address of the restaurant
    location = models.CharField(max_length=255)
    # Restaurant's contact phone number
    contact_number = models.CharField(max_length=24, unique=True)
    # Average user rating for the restaurant
    rating = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    # URL or reference to an image representing the restaurant
    restaurant_image = models.ImageField(null=True, blank=True)
    # Counter for consecutive winning days
    winning_strike = models.IntegerField(default=0)

    class Meta:
        """ class meta for ordering restaurant objects based on rating """
        ordering = ['-rating']

    @property
    def is_highly_rated(self):
        """
        Checks if the restaurant has a high rating.
        """
        return self.rating is not None and self.rating >= 4.5

    def __str__(self):
        """ string representation of restaurant """
        return str(self.restaurant_name)


class Menu(models.Model):
    """ Menu model to represent the menu object with proper fileds and their relationships """

    # ID of the associated restaurant
    restaurant = models.ForeignKey(
        Restaurant,
        related_name='dish_menus',
        on_delete=models.CASCADE
    )
    # Name of the dish or food item
    dish_name = models.CharField(max_length=255, unique=True)
    # Brief summary of the dish
    description = models.TextField(null=True, blank=True)
    # Price of the dish
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # Date for which the menu is applicable
    date = models.DateField(auto_now_add=True)

    class Meta:
        """ For ordering menus """
        ordering = ['dish_name']

    def __str__(self):
        return str(self.dish_name)


class Vote(models.Model):
    """ 
        Vote model which will count
        Employee's votes on specific menu  
    """

    # ID of the user casting the vote
    voter = models.ForeignKey(
        CustomUser,
        related_name='votes',
        on_delete=models.CASCADE
    )
    # ID of the menu for which the vote is cast
    menu = models.ForeignKey(
        Menu,
        related_name='votes',
        on_delete=models.CASCADE
    )
    # Timestamp indicating when the vote was cast
    vote_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Ordering based on timestamp """
        ordering = ['-vote_timestamp']

    def __str__(self):
        return f"Voter - {self.voter} || Menu - {self.menu}"


class Feedback(models.Model):
    """ Feedbacks of user on specific menu """

    # ID of the user providing feedback
    employee = models.ForeignKey(
        CustomUser,
        related_name='feedbacks',
        on_delete=models.CASCADE
    )
    # ID of the related menu (references Menus.MenuID)
    menu = models.ForeignKey(
        Menu,
        related_name='feedbacks',
        on_delete=models.CASCADE
    )
    # Date and time when the feedback was submitted
    date_time = models.DateTimeField(auto_now_add=True)
    # Actual feedback comments or text
    feedback_text = models.TextField()

    class Meta:
        """ Ordering feedbacks based on timestamp """
        ordering = ['date_time']

    def __str__(self):
        return str(self.feedback_text)


class DailyResults(models.Model):
    """ Daily results based on the votes of employees """

    # ID of the winning menu for the day
    winning_menu = models.ForeignKey(
        Menu,
        related_name='results',
        on_delete=models.CASCADE
    )
    # ID of the restaurant with the winning menu
    winning_restaurant = models.ForeignKey(
        Restaurant,
        related_name='results',
        on_delete=models.CASCADE
    )
    # Date for which the results are applicable
    result_date = models.DateField(auto_now_add=True)
    # The total number of votes received on that day
    votecount = models.IntegerField()

    class Meta:
        """ Result ordering based on dates """
        ordering = ['-result_date']

    def __str__(self):
        return f"Winning Restaurant - {self.winning_restaurant} || Total Votes - {self.votecount}"
