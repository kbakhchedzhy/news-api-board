from django.db import models


class News(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)
    link = models.TextField()
    creation_date = models.DateTimeField()
    amount_of_votes = models.IntegerField()
    author_name = models.TextField(max_length=100)


class Comments(models.Model):

    author_name = models.TextField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField()
    news = models.ForeignKey("home.News", on_delete=models.CASCADE)
