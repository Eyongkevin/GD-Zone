from django.test import TestCase
from django.urls import resolve
from .utils import accumulative_percentage
from .templatetags.workspace_tags import round_up
from .views import accumulative_percentage_view

# Create your tests here.
class TestWorkspaceFunc(TestCase):
    def test_accumulative_percentage_pass(self):
        amount = 500
        percentage = 10
        period = 14

        result = 1898.7491679162047

        self.assertEqual(
            accumulative_percentage(
                amount=amount, percentage=percentage, period=period
            ),
            result,
        )

    def test_round_up_2_decimals(self):
        amount = 1898.7491679162047
        decimal_number = 2

        result = 1898.75

        self.assertEqual(round_up(amount, decimal_number), result)


class TestWorkspaceUrls(TestCase):
    def test_accu_percentage_uses_correct_view(self):
        url = resolve("/workspace/accu-percentage/")
        self.assertEqual(url.func, accumulative_percentage_view)
