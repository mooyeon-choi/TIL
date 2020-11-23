from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    # path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/comments/create/', views.comment_create, name='comment_content'),
    path('<int:article_pk>/comments/<int:comment_pk>/comment_delete/', views.comment_delete, name='comment_delete'),
    path('<int:article_pk>/like/', views.like, name='like')
]