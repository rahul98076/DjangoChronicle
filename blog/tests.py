from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostTests(TestCase):
    # This special method runs before each test function.
    # We use it to set up the data our tests will need.
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.post = Post.objects.create(
            title="A Test Post Title",
            slug="a-test-post",
            author=self.user,
            content="Some test content.",
            status="published",
        )

    # All test methods must start with 'test_'.
    def test_post_model_str(self):
        """Test the string representation of the Post model."""
        self.assertEqual(str(self.post), "A Test Post Title")

    def test_homepage_status_code(self):
        """Test that the homepage loads correctly and returns a 200 status code."""
        # self.client is a dummy web browser we can use for testing.
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_contains_post(self):
        """Test that a published post's title appears on the homepage."""
        response = self.client.get("/")
        self.assertContains(response, "A Test Post Title")
