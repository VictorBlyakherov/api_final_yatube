from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)
router.register('api/v1/follow', FollowViewSet)
router.register(r'api/v1/posts/(?P<pk1>[^/.]+)/comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
