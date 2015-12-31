# coding: utf-8
from __future__ import unicode_literals, absolute_import
from remind.views import RemindDetailView, RemindListView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', RemindListView.as_view(), name='remind_list'),
    url(r'^(?P<pk>\w{32})$', RemindDetailView.as_view(), name='remind_detail'),
]