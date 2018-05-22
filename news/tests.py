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