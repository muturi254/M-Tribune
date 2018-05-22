from django.test import TestCase
from .models import Editor, Article, Tags

# Create your tests here.
class EditorTestClas(TestCase):
    def setUp(self):
        self.james = Editor(first_name='James', last_name='Muriuki', email='james@moringaschool.com')

    # test instance 
    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)> 0)

class ArticleTestClass(TestCase):
    def setUp(self):
        self.james = Editor(first_name='James', last_name='Muriuki', email='james@moringaschool.com')
        self.save_editor()

        self.new_tag = Tags(name='hello')
        self.new_tag.save()

        self.new_article = Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        slf.new_article.save()

        self.new_article.tags.add(self.new_tag)

        def tearDown(self):
            Editor.objects.all().delete()
            Article.objects.all().delete()
            Tags.objects.all().delete()

        def test_get_news_today(self):
            todays_news = Article.todays_news()
            self.assertTrue(len(todays_news)> 0)

        