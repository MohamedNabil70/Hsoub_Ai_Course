import re
re.UNICODE

def match_pattern(pattern, string):
    """
    Matches a given pattern against a string using regular expressions.

    Args:
        pattern (str): The regex pattern to match.
        string (str): The string to search within.

    Returns:
        bool: True if the pattern matches the string, False otherwise.
    """
    return re.fullmatch(pattern, string) is not None    


def find_all_matches(pattern, string):
    """
    Finds all occurrences of a pattern in a string.

    Args:
        pattern (str): The regex pattern to search for.
        string (str): The string to search within.

    Returns:
        list: A list of all matches found in the string.
    """
    return re.findall(pattern, string)



print(find_all_matches(r'\d+', 'There are 12 apples 45 4 and 34 oranges.'))  # Example usage

text = "مرحبا 123"
m = re.findall(r'[\u0600-\u06FF]+', text)

print(m)  # Output: ['مرحبا']
