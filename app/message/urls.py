from django.urls import path, include

from rest_framework.routers import DefaultRouter

from message import views


router = DefaultRouter()
router.register('conversation', views.ConversationViewset)

app_name = 'message'

urlpatterns = [
    path('new/', views.CreateMessageView.as_view(), name='new_message'),
    path('', include(router.urls))
]
