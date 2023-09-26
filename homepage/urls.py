from django.urls import path, include

from . import views
# from .views import PostListView, PostDetailView, CategoryListView, CategoryDetailView

urlpatterns = [
    path('', views.index, name='index'),
    # path('bootstrap', views.bootstrap, name='bootstrap'),
    # # Blog Site
    # path('blogs', views.blog, name='blogs'),
    # path('blog', PostListView.as_view(), name='post-list'),
    # path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),

    path('contact/', views.contact_view, name='contact_view'),
    path('contact/success/', views.contact_success, name='contact_success'),  # Create this view/template as needed
]

