from django.test import TestCase
from common.admintest import adminviews_test


class MetricCardTest(TestCase):
    def test_admin_views(self):
        adminviews_test(self)
