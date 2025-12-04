# TODO: Create utility functions here
#
# Functions to implement:
#
# 1. generate_id(prefix) -> string
#    Generate a unique ID with the given prefix
#    Example: generate_id("BK") -> "BK001"
#
# 2. validate_email(email) -> bool
#    Check if email is valid (contains @ and .)
#
# 3. save_to_file(data, filename) -> bool
#    Save data to a JSON file
#    Handle exceptions and return True/False
#
# 4. load_from_file(filename) -> dict or list
#    Load data from a JSON file
#    Return empty dict/list if file doesn't exist
#
# Hint: You may need to import: json, datetime, random, os
#
# Start coding below:

import json,datetime,random,os

def generate_id(prefix) -> str:
    unique_number = random.randint(100, 999)
    return f"{prefix}{unique_number:03d}"

def validate_email(email) -> bool:
    return "@" in email and "." in email

def save_to_file(data, filename) -> bool:
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
        return True
    except Exception as e:
        return False
    
def load_from_file(filename):
    if not os.path.exists(filename):
        return {} if filename.endswith('.json') else []
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        return {} if filename.endswith('.json') else []