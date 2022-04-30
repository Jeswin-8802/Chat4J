from django.db import models

from accounts.models import User

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey('Forum', on_delete = models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + ' - ' + self.user.username

class Forum(models.Model):
    admin = models.CharField(help_text='Username of the user that created this FORUM', max_length = 25, null = False)
    participants = models.ManyToManyField(User, blank = True)
    messages = models.ManyToManyField(Message, blank=True)
    name = models.CharField(max_length = 50)
    description = models.TextField(help_text='Forum Description', null = True)
    image = models.ImageField(help_text='Forum Picture', blank=True, upload_to='forum_pic')

    def __str__(self):
        return self.name