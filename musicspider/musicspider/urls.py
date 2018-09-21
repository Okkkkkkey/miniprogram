from django.conf.urls import include, url
from django.contrib import admin
from search import views as sv

urlpatterns = [
    # Example
    # url(r'^$', 'musicspider.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', sv.search),
]
