from django.urls import path
from .views import AuthorCreateView, AuthorUpdateView, AuthorDeleteView, ArticleView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ArticleView.as_view(), name='article'),
    path('new/', AuthorCreateView.as_view(), name='author_create'),
    path('<int:pk>/update', AuthorUpdateView.as_view(), name='author_update'),
    path('<int:pk>/delete', AuthorDeleteView.as_view(), name='author_delete'),

    ]
