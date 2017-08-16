from django.conf.urls import url, include

from myapp.views import MyView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', MyView.as_view(), name='my-view'),
]
