from ..models import Post, Tag
from rest_framework.serializers import ModelSerializer

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class PostSerializer(ModelSerializer):

    # tags = TagSerializer(many=False, read_only=True)
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['tag', 'title', 'slug', 'content', 'created_on']