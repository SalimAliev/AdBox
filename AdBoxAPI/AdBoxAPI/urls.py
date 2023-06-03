import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from Ad.views import ad_view_list, ad_view, ad_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advertisements/', ad_view_list),
    path('advertisements/<int:pk>', ad_view),
    path('advertisements/create/', ad_create),

    path('__debug__/', include(debug_toolbar.urls)),
]


