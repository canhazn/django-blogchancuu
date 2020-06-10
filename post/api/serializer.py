from ..models import Post, Tag
from rest_framework.serializers import ModelSerializer

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        
class PostSerializer(ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['tags', 'title', 'slug', 'content', 'created_on']