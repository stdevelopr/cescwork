from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.CharField(max_length=500)
	about = models.CharField(max_length=1000)

	def __str__(self):
		return self.user.username

class Work(models.Model):
	CATEGORY_CHOICES = (
		("GD", "Graphics & Design"),
		("DM", "Digital % Marketing"),
		("VA", "Video & Animation"),
		("MA", "Music & Audio"),
		("GD", "Programming & Tech")
	)

	title = models.CharField(max_length=500)
	category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
	description=models.CharField(max_length=1000)
	price = models.IntegerField(default=6)
	photo = models.FileField(upload_to='work')
	status = models.BooleanField(default=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User', null=True)
	create_time = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title