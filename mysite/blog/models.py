from django.db import models
from hvad.models import TranslatableModel, TranslatedFields

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


class Autor(TranslatableModel):
    name = models.CharField(max_length=25)

    translations = TranslatedFields(
        libro = models.CharField(max_length=25),
    )
