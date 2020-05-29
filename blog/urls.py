from django.urls import path
from .views import PostListView, post_share, post_detail

app_name = 'blog'

urlpatterns = [
    # post views
    path('', PostListView.as_view(), name='post_list'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail,
         name='post_detail'),
]
