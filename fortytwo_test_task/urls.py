from django.conf.urls import patterns, include, url
from apps.mainp.views import Index
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Index.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
