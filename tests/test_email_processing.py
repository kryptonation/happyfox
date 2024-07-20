# test_email_processing.py

import unittest
from datetime import datetime

from models import Email
from process_emails import rule_applies

class TestEmailProcessing(unittest.TestCase):
    """
    Unit tests for email processing logic.
    """

    def test_rule_applies_all_true(self):
        """
        Test case where all conditions are true and the rule applies.
        """
        email = Email(from_address='test@example.com', subject='Test', message='Hello', received_date=datetime.now())
        rule = {
            'conditions': [{'field': 'from_address', 'predicate': 'equals', 'value': 'test@example.com'}],
            'predicate': 'All',
            'actions': ['mark_as_read']
        }
        self.assertTrue(rule_applies(email, rule))

    def test_rule_applies_any_true(self):
        """
        Test case where at least one condition is true and the rule applies.
        """
        email = Email(from_address='test@example.com', subject='Test', message='Hello', received_date=datetime.now())
        rule = {
            'conditions': [{'field': 'from_address', 'predicate': 'equals', 'value': 'test@example.com'},
                           {'field': 'subject', 'predicate': 'equals', 'value': 'Non-matching subject'}],
            'predicate': 'Any',
            'actions': ['mark_as_read']
        }
        self.assertTrue(rule_applies(email, rule))

    def test_rule_applies_all_false(self):
        """
        Test case where not all conditions are true and the rule does not apply.
        """
        email = Email(from_address='test@example.com', subject='Test', message='Hello', received_date=datetime.now())
        rule = {
            'conditions': [{'field': 'from_address', 'predicate': 'equals', 'value': 'non_matching@example.com'}],
            'predicate': 'All',
            'actions': ['mark_as_read']
        }
        self.assertFalse(rule_applies(email, rule))

    def test_rule_applies_any_false(self):
        """
        Test case where none of the conditions are true and the rule does not apply.
        """
        email = Email(from_address='test@example.com', subject='Test', message='Hello', received_date=datetime.now())
        rule = {
            'conditions': [{'field': 'from_address', 'predicate': 'equals', 'value': 'non_matching@example.com'},
                           {'field': 'subject', 'predicate': 'equals', 'value': 'Non-matching subject'}],
            'predicate': 'Any',
            'actions': ['mark_as_read']
        }
        self.assertFalse(rule_applies(email, rule))

if __name__ == '__main__':
    unittest.main()
