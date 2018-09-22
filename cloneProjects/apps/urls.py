from django.urls import path
from apps import views

urlpatterns=[
    path('about/',views.AboutPage.as_view(),name='about'),
    path('',views.PostList.as_view(),name='post_list'),
    path('detail/<int:pk>/',views.PostDetail.as_view(),name='post_detail'),
    path('post/new/',views.PostCreate.as_view(),name='post_new'),
    path('post/edit/<int:pk>/',views.PostUpdate.as_view(),name='post_edit'),
    path('post/remove/<int:pk>/',views.PostDelete.as_view(),name='post_remove'),
    path('post/draftList/',views.PostDraftList.as_view(),name='post_draft_list'),
    path('post/publish/<int:pk>/',views.post_publish,name='post_publish'),
    path('post/comment/<int:pk>/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/approve/<int:pk>/',views.comment_approve,name='comment_approve'),
    path('comment/remove/<int:pk>/',views.comment_remove,name='comment_remove')
]
