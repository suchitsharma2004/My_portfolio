from django.urls import path
from .views import home, projects, contact, llm_chat, llm_test, health_check, simple_test, home_complex

urlpatterns = [
    path('', home, name='home'),
    path('macos/', home_complex, name='home_complex'),  # Test complex template
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('api/llm-chat/', llm_chat, name='llm_chat'),
    path('api/llm-test/', llm_test, name='llm_test'),
    path('health/', health_check, name='health_check'),
    path('test/', simple_test, name='simple_test'),
]
