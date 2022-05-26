from rest_framework import serializers
from sesh.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'area', 'difficulty', 'time', 'players_needed', 'description', 'player')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['player'] =  {'username': instance.player.user_name, 'id': instance.player.id}
        return ret

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'area', 'difficulty', 'time', 'players_needed', 'description', 'player')
