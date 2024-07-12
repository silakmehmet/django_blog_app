from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryMVS, PostMVS

router = DefaultRouter()
router.register("categories", CategoryMVS)
router.register("posts", PostMVS)

urlpatterns = [

]+router.urls
