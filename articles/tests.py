from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Article

User = get_user_model()


class UserModelTest(TestCase):

    def test_create_user(self):
        email = 'test@example.com'
        password = 'password123'
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        email = 'superuser@example.com'
        password = 'password123'
        superuser = User.objects.create_superuser(email=email, password=password)

        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.check_password(password))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_user_role(self):
        email = 'roleuser@example.com'
        password = 'password123'
        user = User.objects.create_user(email=email, password=password, role='author')

        self.assertEqual(user.role, 'author')


class ArticleModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='author@example.com', password='password123', role='author')

    def test_create_article(self):
        title = 'Test Article'
        content = 'This is a test article.'
        article = Article.objects.create(
            title=title,
            content=content,
            author=self.user,
            is_published=True,
            is_private=False
        )

        self.assertEqual(article.title, title)
        self.assertEqual(article.content, content)
        self.assertEqual(article.author, self.user)
        self.assertTrue(article.is_published)
        self.assertFalse(article.is_private)



