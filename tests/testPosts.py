import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from random import randint

from blog.models import Post, Category


def create_post(title, days):
    """
    Create a post with the given `title` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    category = Category.objects.create(title='category', slug='category')
    return Post.objects.create(title=title,
                               date_published=time,
                               category_id=category.id,
                               slug=title.replace(' ', '-').lower())


class PostIndexViewTests(TestCase):
    def test_no_posts(self):
        """
        If no posts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no posts")
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_past_post(self):
        """
        Post with a date_published in the past are displayed on the
        index page.
        """
        create_post(title="Past post", days=-30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['posts'],
            ['<Post: Past post>']
        )

    def test_future_post(self):
        """
        Questions with a date_published in the future aren't displayed on
        the index page.
        """
        create_post(title="Future post", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, "There are no posts")
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_future_and_past_posts(self):
        """
        Questions with a date_published in the future aren't displayed on
        the index page, and post with a date_published in the past are displayed on the
        index page.
        """
        create_post(title="Future post", days=30)
        create_post(title="Past post", days=-30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['posts'],
            ['<Post: Past post>']
        )