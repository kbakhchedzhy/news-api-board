from celery import shared_task

from app.models import News


@shared_task
def reset_votes():
    posts = News.objects.all()
    for post in posts:
        post.amount_of_votes = 0
        post.save()
