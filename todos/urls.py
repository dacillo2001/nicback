from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # This registers the '/tasks/' endpoint

urlpatterns = [
    path('', include(router.urls)),  # This should include all the URLs from the router
]
