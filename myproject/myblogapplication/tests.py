from django.test import TestCase
from django.urls import reverse
from .models import BlogPost, Comment

class BlogPostTests(TestCase):
    def setUp(self):
        self.post = BlogPost.objects.create(
            title="Books",
            content="Best books"
        )

    def test_post_creation(self):
        self.assertEqual(BlogPost.objects.count(), 1)
        self.assertEqual(self.post.title, "Books")

    def test_post_edit(self):
        self.post.title = "Livres"
        self.post.save()
        updated_post = BlogPost.objects.get(id=self.post.id)
        self.assertEqual(updated_post.title, "Livres")

    def test_post_delete(self):
        self.post.delete()
        self.assertEqual(BlogPost.objects.count(), 0)

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.content)

class CommentTests(TestCase):
    def setUp(self):
        self.post = BlogPost.objects.create(
            title="Books",
            content="10 meilleurs livres"
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author="Emilie",
            text="Cool !"
        )

    def test_comment_creation(self):
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(self.comment.text, "Cool !")

    def test_comment_edit(self):
        self.comment.text = "Vraiment intéressant"
        self.comment.save()
        updated_comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(updated_comment.text, "Vraiment intéressant")

    def test_comment_delete(self):
        self.comment.delete()
        self.assertEqual(Comment.objects.count(), 0)

    def test_add_comment_view(self):
        response = self.client.post(
            reverse('add_comment', args=[self.post.id]),
            {'author': 'Camille', 'text': 'Nice!'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 2)
