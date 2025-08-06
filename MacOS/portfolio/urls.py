from django.urls import path
from .views import home, projects, contact, llm_chat, llm_test, health_check, simple_test

urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('api/llm-chat/', llm_chat, name='llm_chat'),
    path('api/llm-test/', llm_test, name='llm_test'),
    path('health/', health_check, name='health_check'),
    path('test/', simple_test, name='simple_test'),
]
