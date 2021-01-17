from rest_framework import routers

from home.api_views import PersonViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('person', PersonViewSet, basename='person')
