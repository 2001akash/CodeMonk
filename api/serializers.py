# api/serializers.py

from rest_framework import serializers
from .models import User, Paragraph, Word

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'dob', 'date_joined', 'last_login']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'text', 'created_at', 'updated_at']

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'value', 'paragraph']