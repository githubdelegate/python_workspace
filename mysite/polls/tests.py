from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime
# Create your tests here.

class QuestionModelTests(TestCase):
    
    def test_was_publised_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_publised_recently(),False)
