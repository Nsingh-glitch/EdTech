from django.urls import path
from quiz_api.views import chat_gpt
from .views import  quiz_progress_api,quiz_view,progress

urlpatterns = [
    path('', quiz_view, name='quiz'),
    path('chat/', chat_gpt, name='chat_gpt'),

    path('progress/', progress, name='progress'),
    
]
