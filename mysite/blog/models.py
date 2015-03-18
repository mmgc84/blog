from django.db import models

# Create your models here.


class Post(models.Model):
    post_author = models.CharField(max_length=20)
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.post_title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment_author = models.CharField(max_length=20)
    comment_text = models.TextField()
    comment_pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.comment_text
