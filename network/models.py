from django.contrib.auth.models import AbstractUser
from django.db import models
from auctions.models import User


class posts(models.Model):
	sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name="emails_sent")
	body = models.TextField(blank=True)
	likes=models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)
	def serialize(self):
		return{
		"id": self.id,
	    "sender": self.sender.username,
	    "body": self.body,
	    "timestamp": self.timestamp.strftime("%b %-d %Y, %-I:%M %p"),
	    "like":self.likes,
		}
class comments(models.Model):
	comment=models.CharField(max_length=128)
	post=models.ForeignKey(posts,on_delete=models.CASCADE,related_name="pp")
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="usera")
class following(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="mana")
	people=models.ForeignKey(User,on_delete=models.CASCADE,related_name="peoplea")
	class Meta:constraints=[models.UniqueConstraint(fields=['user','people'],name='unique_following')]
class Todo_likes(models.Model):
	
    todo = models.ForeignKey(posts, on_delete=models.CASCADE, related_name="like_post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like_user")
    class Meta:constraints=[models.UniqueConstraint(fields=['todo','user'],name='unique_like')]