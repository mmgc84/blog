from django.db import models

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=None)
    post_text = models.TextField()
    pub_date = models.DateTimeField('date_published')


class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment_text = models.TextField()
