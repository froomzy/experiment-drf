from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'$', views.ApplicationView.as_view(), name='application-list'),
    url(r'(?P<pk>\d+)$', views.ApplicationDetailView.as_view(), name='application-detail'),
]
