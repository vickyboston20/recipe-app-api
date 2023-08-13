"""
Test for Recipe models.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from recipe import models


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
