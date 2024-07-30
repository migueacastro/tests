from django.urls import path
from films.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('films', FilmViewSet, basename='films')

urlpatterns = router.urls

urlpatterns += [
    path('register/', RegistrarionAPIView.as_view())
]


#urlpatterns = [
#    path('films/', FilmListAPIView.as_view()), # / api / films
#   path('films/<int:pk>/', FilmDetailAPIView.as_view())
#]