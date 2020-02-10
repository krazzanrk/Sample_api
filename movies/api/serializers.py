from rest_framework import serializers
from ..models import *


class GenreSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=25)
    created_date = serializers.DateField(read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    modified_by = serializers.ReadOnlyField(source='modified_by.username')
    modified_date = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data, created_by_id=self.context['request'].user.id)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.modified_by_id = self.context['request'].user.id
        instance.save()
        return instance


class FilmSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='created_by.username')
    modifier = serializers.ReadOnlyField(source='modified_by.username')

    class Meta:
        model = Film
        fields = ['title', 'cover_image', 'released_date', 'genre', 'creator', 'modifier']


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        account = User(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"password": "password does not  match"})

        account.set_password(password)
        account.save()
        return account
