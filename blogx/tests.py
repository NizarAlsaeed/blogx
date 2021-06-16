from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Article
# Create your tests here.
class ArticleTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='tester',
        email='tester@test.com',
        password='test',
        )

        self.article = Article.objects.create(
        title='testarticle',
        author = self.user,
        content = 'testing Content',
        )

    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '_base.html')
        self.assertTemplateUsed(response, 'blogx/home.html')

    def test_article_detail(self):
        url = reverse('article', args='1')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '_base.html')
        self.assertTemplateUsed(response, 'blogx/article.html')

    def test_article_create(self):
        url = reverse('author_create')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '_base.html')
        self.assertTemplateUsed(response, 'blogx/author_create.html')

    def test_article_update(self):
        url = reverse('author_update', args='1')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '_base.html')
        self.assertTemplateUsed(response, 'blogx/author_update.html')

    def test_article_delete(self):
        url = reverse('author_delete', args='1')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '_base.html')
        self.assertTemplateUsed(response, 'blogx/author_delete.html')
