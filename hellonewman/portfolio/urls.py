from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$',
        view = 'hellonewman.portfolio.views.gallery_detail',
        name = 'gallery-detail'
    ),
    url(r'^category/(?P<slug>[-\w]+)/$',
        view = 'hellonewman.portfolio.views.category_list',
        name = 'category-list'
    ),
    url(r'^$',
        view = 'hellonewman.portfolio.views.gallery_home',
        name = "gallery-home"),
)

