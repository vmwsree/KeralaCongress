from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
url(r'^Kerala-Yathra/$', 'keralayathra.views.keralayathra', name='yathra'),
url(r'^Kerala-Yathra/(?P<day_id>\d+)/$', 'keralayathra.views.yathraDay', name='day'),
url(r'^Gallery/$', 'keralayathra.views.gallery'),
url(r'^News/$', 'keralayathra.views.news'),
url(r'^News/(?P<news_id>\d+)/$', 'keralayathra.views.newsitem'),
)