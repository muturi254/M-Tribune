from django.conf.urls import url
from . import views

# write zyou views here
urlpatterns=[
    # url(r'^$', views.welcome, name='welcome'),
    url(r'^$', views.news_of_day, name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_news, name='pastNews'),
    url(r'^search/$', views.search_results, name='search_results'),
]
