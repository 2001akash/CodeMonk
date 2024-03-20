# api/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db.models import Count
from .models import User, Paragraph, Word
from .serializers import UserSerializer, ParagraphSerializer, WordSerializer
from .utils import tokenize_paragraphs

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ParagraphCreateView(generics.CreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        text = request.data.get('text')
        paragraphs = tokenize_paragraphs(text)
        serializer_data = [{'text': paragraph} for paragraph in paragraphs]
        serializer = self.get_serializer(data=serializer_data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        paragraph_instances = serializer.instances
        words = []
        for paragraph in paragraph_instances:
            for word in tokenize_paragraphs(paragraph.text):
                words.append(Word(value=word.lower(), paragraph=paragraph))
        Word.objects.bulk_create(words)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TopParagraphsView(generics.ListAPIView):
    serializer_class = ParagraphSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        word = self.request.query_params.get('word', '').lower()
        if word:
            word_objects = Word.objects.filter(value=word)
            paragraph_ids = word_objects.values('paragraph_id').annotate(count=Count('id')).order_by('-count').values_list('paragraph_id', flat=True)[:10]
            paragraphs = Paragraph.objects.filter(id__in=list(paragraph_ids))
        else:
            paragraphs = Paragraph.objects.all()
        return paragraphs