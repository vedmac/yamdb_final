from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    EmailRegistrationView, TokenObtainView, UsersViewSet,
    ReviewViewSet, CategoriesViewSet, CommentViewSet,
    GenresViewSet, TitlesViewSet)

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='Users')
router.register('titles/(?P<titles_id>.+)/reviews', ReviewViewSet,
                basename='reviews-list')
router.register('titles/(?P<titles_id>.+)/reviews/(?P<reviews_id>.+)/comments',
                CommentViewSet, basename='comments-list')
router.register('titles', TitlesViewSet, basename='titles')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')

auth_urlpatterns = [
    path('email/', EmailRegistrationView.as_view()),
    path('token/', TokenObtainView.as_view()),
]

urlpatterns = [
    path('v1/auth/', include(auth_urlpatterns)),
    path('v1/', include(router.urls)),
]
