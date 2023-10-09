from rest_framework.serializers import ModelSerializer
from users.api.serializers import UserSerializer
from posts.api.serializers import PostSerializer

from comments.models import Comment

class CommentSerializer(ModelSerializer):
  # user = UserSerializer()
  # post = PostSerializer()
  
  class Meta:
    model = Comment
    fields = ['content', 'created_at', 'user', 'post']