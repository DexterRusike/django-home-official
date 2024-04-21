from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username

DayChoices = (
    ('Monday', 'MONDAY'),
    ('Tuesday', 'TUESDAY'),
    ('Wednesday', 'WEDNESDAY'),
    ('Thursday', 'THURSDAY'),
    ('Friday', 'FRIDAY'),
    ('Saturday', 'SATURDAY'),
    ('Sunday', 'SUNDAY')
)

class HomeTimesheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chore_name = models.CharField(max_length=264)
    day = models.CharField(max_length=164, choices=DayChoices, default='Monday')
    
    def calculate_salary(self):
        
        chore_to_number = {
            'Hoovering': 3,
            'Dinner Plates': 3,
            'Dinner': 5,
            'Breakfast': 3,
            'Car': 10,
            'Bins':5,
        }
        
        chore_number = chore_to_number.get(self.chore_name, 0)
        
        number = 0
        number += chore_number
        
        return number
    
class HomeGroceries(models.Model):
    name = models.CharField(max_length=264)
    
class HomeBooksToRead(models.Model):
    book_name = models.CharField(max_length=264)
    description = models.TextField()
    photo = models.ImageField(upload_to='books')
    
class HomeGoals(models.Model):
    goal_name = models.CharField(max_length=264)
    description = models.TextField()
    accomplied_date = models.DateField()
    
class HomeEvents(models.Model):
    event_name = models.CharField(max_length=264)
    date = models.DateField()
    description = models.TextField()
    by_who = models.OneToOneField(User, on_delete=models.CASCADE)