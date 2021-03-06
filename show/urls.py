from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/department_list/', views.get_department_list),
    url(r'^api/department/', views.get_department),
    url(r'^api/one_department/', views.get_one_department),

    url(r'^api/story/', views.get_story),

    url(r'^api/member_list/', views.get_member_list),
    url(r'^api/member/', views.get_member_of_the_year_and_department),

    url(r'^api/work/', views.get_work),

    url(r'^api/comment_list/', views.comment_list),
    url(r'^api/comment/', views.comment),
]

