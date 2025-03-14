from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register("", PostViewSet, basename="posts") 
router.register("users", UserViewSet, basename="users") 

urlpatterns = router.urls
