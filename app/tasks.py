from celery import shared_task

from app.models import News


@shared_task
def reset_post_votes_count():
    posts = News.objects.all()
    for post in posts:
        post.votes.clear()

