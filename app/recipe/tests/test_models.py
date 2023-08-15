"""
Test for Recipe models.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from recipe import models


def create_user(email='user@example.com', password='testpass123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test models."""

    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Smaple recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description="Sample recipe description.",
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test Creating a tag is successful."""
        user = create_user()
        tag = models.Tag.objects.create(
            user=user,
            name='Tag1'
        )

        self.assertEqual(str(tag), tag.name)
