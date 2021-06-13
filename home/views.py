from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from home.models import News, Comments
from home.serializers import NewsSerializer, CommentsSerializer


class NewsViewSet(ModelViewSet):
    """
    CRUD operations of news
    """

    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CommentsViewSet(ModelViewSet):
    """
    CRUD operations of comment
    """

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class VoteForNews(APIView):
    """
    Edit amount of votes of news model.
    """

    def get(self, request, pk):
        news = News.objects.get(id=pk)
        news.amount_of_votes += 1
        news.save()
        return HttpResponseRedirect(
            redirect_to="http://0.0.0.0:8000/drf/news/1/"
        )  # noqa
