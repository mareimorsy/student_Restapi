from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^student/$', views.students_list),
    url(r'^student/(?P<pk>[0-9]+)/$', views.students_detail),
]
