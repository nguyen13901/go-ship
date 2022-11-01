from atexit import register
from rest_framework import routers

from api_user.views.user import ResgisterAPIView
from .views import *

app_name = 'api_user'
router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename="user")
# router.register(r'register/', ResgisterAPIView.as_view() , basename="user")
urlpatterns = router.urls