from django.urls import path
from .views import AuthorHomeView, AuthorCreateView, AuthorArticleView, ArticleView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ArticleView.as_view(), name='article'),
    # path('', AuthorHomeView.as_view(), name='author_home'),
    # path('', AuthorCreateView.as_view(), name='author_create'),
    # path('', AuthorArticleView.as_view(), name='author_article'),
    ]
