import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from Ad.views import AdAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advertisements/', AdAPIView.as_view()),
    path('advertisements/<int:ad_id>/', AdAPIView.as_view()),
    path('__debug__/', include(debug_toolbar.urls)),
]


