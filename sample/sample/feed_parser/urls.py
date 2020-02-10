from django.urls import include, path
from rest_framework import routers
from feed_parser import views

router = routers.DefaultRouter()
router.register(r'repos', views.RepoViewSet)

urlpatterns = [
    path('', include(router.urls)),
        path('/', include('rest_framework.urls', namespace='rest_framework'))
        ]
