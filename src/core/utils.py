"""Utility functions for the core module."""

def format_message(message: str, prefix: str = "") -> str:
    """Format a message with an optional prefix.
    
    Args:
        message: The message to format
        prefix: Optional prefix to add
        
    Returns:
        Formatted message string
    """
    if prefix:
        return f"{prefix}: {message}"
    return message


def validate_input(value: str) -> bool:
    """Validate input string is not empty and contains only alphanumeric characters.
    
    Args:
        value: String to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not value or not isinstance(value, str):
        return False
    return value.strip() != "" and value.replace(" ", "").isalnum()
