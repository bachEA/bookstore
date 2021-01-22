from django.test import TestCase
from django.contrib.auth.models import User

from .models import Review

# Create your tests here.
class ReviewTests(TestCase):

    test_user_name = "user1"
    test_user_password = "user1@"
    test_review_title = "Solid book"
    test_review_body = "Great read for intermediate Python users"

    # Always use self for the first argument in instance method
    # Always use cls as the first argument in class method

    # classmethod TestCase.setUpTestData()
    # This technique allows for faster tests as compared to using setUp().

    @classmethod
    def setUpTestData(cls):

        # Create a test user
 
        test_user1 = User.objects.create_user(username = cls.test_user_name, password = cls.test_user_password)
        test_user1.save()

        # Create a test review

        test_review1 = Review.objects.create(author = test_user1, title = cls.test_review_title, body = cls.test_review_body)   
        test_review1.save()

    def test_review_content(self):

        review = Review.objects.get(id=1)
        self.assertEqual(self.test_user_name, str(review.author))
        self.assertEqual(self.test_review_title, str(review.title))
        self.assertEqual(self.test_review_body, str(review.body))

        user = User.objects.get(id=1)
        self.assertEqual(self.test_user_name, str(user.username))


