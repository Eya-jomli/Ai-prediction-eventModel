# urls.py
from django.contrib import admin
from django.urls import path
from .chatbotView import chat
from .eventView import predict_top_events


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', chat, name='chatbot'),
    path('predict_top_events/', predict_top_events, name='predict_top_events'),

]
