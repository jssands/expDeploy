from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin

urlpatterns = [
	url(r'^api/', include('expdeploy.api.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', RedirectView.as_view(url='/testapp/', permanent=False)),
    url(r'^testapp/', include('expdeploy.testapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
