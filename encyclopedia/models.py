from django.db import models
from django.urls import reverse
from auctions.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Event(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userk")
	title = models.CharField(max_length=200)
	description = models.TextField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	@property
	def get_html_url(self):
		url = reverse('wiki:event_edit', args=(self.id,))
		return f'<a href="{url}"> {self.title} </a>'
#events