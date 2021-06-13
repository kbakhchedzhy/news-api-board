from rest_framework import serializers

from home.models import News, Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:

        model = Comments
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):

    comments = CommentsSerializer(
        many=True,
        required=False,
        read_only=True,
    )

    class Meta:

        model = News
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_votes",
            "author_name",
            "comments",
        ]
        read_only_fields = ["creation_date", "amount_of_votes"]

    def create(self, validated_data):
        return News.objects.create(**validated_data, amount_of_votes=0)
