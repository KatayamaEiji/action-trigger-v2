from django.views.generic import TemplateView
from django.views.generic import ListView
from ..models import Post # Postモデルをimport

class IndexView(TemplateView):
    template_name = 'acounts/index.html'

class PostListView(ListView): # generic の ListViewクラスを継承
    model = Post # 一覧表示させたいモデルを呼び出し