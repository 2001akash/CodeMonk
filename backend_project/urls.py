# api/urls.py

from django.urls import path, include
from api import views

urlpatterns = [
    path('api/auth/', include('rest_framework.urls')),
    path('api/users/', views.UserCreateView.as_view(), name='user-create'),
    path('api/paragraphs/', views.ParagraphCreateView.as_view(), name='paragraph-create'),
    path('api/top-paragraphs/', views.TopParagraphsView.as_view(), name='top-paragraphs'),
]