#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-09-05 12:01:43


from django.conf.urls import url
from . import views

urlpatterns = [
    url('^basicmodel/$', views.BasicModelView.as_view()),
    url('^basicmodel/(?P<pk>\d+)/$', views.BasicModelDetailView.as_view()),
    url(r'^file/$', views.FileView.as_view()),
]