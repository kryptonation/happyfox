import json
from models import Email, session
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_rules():
    """
    Loads rules from the JSON file.
    
    Returns:
        list: A list of rules.
    """
    try:
        with open('rules.json') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading rules: {e}")
        return []

def process_email(email, rules):
    """
    Processes an email based on the given rules.
    
    Args:
        email: The email object to process.
        rules: A list of rules to apply to the email.
    """
    for rule in rules:
        if rule_applies(email, rule):
            logger.info(f"Applying rule {rule} to email from {email.from_address} with subject '{email.subject}'")
            apply_actions(email, rule['actions'])

def rule_applies(email, rule):
    """
    Checks if a rule applies to an email.
    
    Args:
        email: The email object.
        rule: The rule to check.
    
    Returns:
        bool: True if the rule applies, False otherwise.
    """
    conditions = rule['conditions']
    predicate = rule['predicate']
    if predicate == 'All':
        return all(match_condition(email, condition) for condition in conditions)
    elif predicate == 'Any':
        return any(match_condition(email, condition) for condition in conditions)

def match_condition(email, condition):
    """
    Matches a single condition against an email.
    
    Args:
        email: The email object.
        condition: The condition to match.
    
    Returns:
        bool: True if the condition matches, False otherwise.
    """
    field = condition['field']
    predicate = condition['predicate']
    value = condition['value']
    email_value = getattr(email, field)
    if predicate == 'contains':
        return value in email_value
    elif predicate == 'not contains':
        return value not in email_value
    elif predicate == 'equals':
        return email_value == value
    elif predicate == 'not equals':
        return email_value != value

def apply_actions(email, actions):
    """
    Applies actions to an email.
    
    Args:
        email: The email object.
        actions: A list of actions to apply.
    """
    for action in actions:
        if action == 'mark_as_read':
            mark_as_read(email)
        elif action == 'mark_as_unread':
            mark_as_unread(email)

def mark_as_read(email):
    """
    Marks an email as read.
    
    Args:
        email: The email object.
    """
    logger.info(f"Marking email {email.id} as read")

def mark_as_unread(email):
    """
    Marks an email as unread.
    
    Args:
        email: The email object.
    """
    logger.info(f"Marking email {email.id} as unread")

def main():
    rules = load_rules()
    emails = session.query(Email).all()
    for email in emails:
        process_email(email, rules)

if __name__ == "__main__":
    main()
