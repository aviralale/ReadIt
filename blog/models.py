from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title= models.CharField(max_length=300)
    content= models.TextField()

    CATEGORY_CHOICES = (
        ('world', 'World'),
        ('miscellaneous', 'Miscellaneous'),
        ('technology', 'Technology'),
        ('design', 'Design'),
        ('culture', 'Culture'),
        ('business', 'Business'),
        ('politics', 'Politics'),
        ('opinion', 'Opinion'),
        ('science', 'Science'),
        ('programming', 'Programming'),
        ('style', 'Style'),
        ('travel', 'Travel'),
    )
    views = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to="blog/thumbnails",default="")
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    slug = models.SlugField(max_length=1000,default='')
    author = models.CharField(max_length=100,default="ReadIt")
    timeStamp = models.DateTimeField(blank=True)
    def __str__(self):
        return self.title + ' by ' + self.author



# sno
# comment
# User
# post
# parent
# timestamp
class blogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + " by " + self.user.username
    