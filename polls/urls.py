from django.conf.urls import url

from . import views

app_name = 'polls_app'
urlpatterns = [
    # ex: /polls_app/
    url(r'^$', views.IndexView.as_view(), name="index"),
    # ex: /polls_app/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls_app/5/results
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls_app/5/votes
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
