from rest_framework import serializers

from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at"
        )
        model = Post
    
    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)

