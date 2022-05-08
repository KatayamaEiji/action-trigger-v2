from django.test import TestCase
from django.urls import reverse, resolve
from ..views.postlist import PostListView

class TestUrls(TestCase):

  """Post 一覧ページへのリダイレクトをテスト"""
  def test_post_list_url(self):
    view = resolve('/post_list/')
    self.assertEqual(view.func.view_class, PostListView)