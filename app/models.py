from django.db import models


class News(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)
    link = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_votes = models.IntegerField(null=True)
    author_name = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class Comments(models.Model):

    id = models.AutoField(primary_key=True)
    author_name = models.TextField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(
        "app.News", on_delete=models.CASCADE, related_name="comments"
    )
