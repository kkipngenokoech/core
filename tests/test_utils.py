"""Tests for core utility functions."""

import pytest
from src.core.utils import format_message, validate_input


class TestFormatMessage:
    """Test cases for format_message function."""
    
    def test_format_message_with_prefix(self):
        """Test formatting message with prefix."""
        result = format_message("Hello world", "INFO")
        assert result == "INFO: Hello world"
    
    def test_format_message_without_prefix(self):
        """Test formatting message without prefix."""
        result = format_message("Hello world")
        assert result == "Hello world"
    
    def test_format_message_empty_prefix(self):
        """Test formatting message with empty prefix."""
        result = format_message("Hello world", "")
        assert result == "Hello world"


class TestValidateInput:
    """Test cases for validate_input function."""
    
    def test_validate_input_valid_string(self):
        """Test validation with valid alphanumeric string."""
        assert validate_input("hello123") is True
    
    def test_validate_input_with_spaces(self):
        """Test validation with spaces (should be valid)."""
        assert validate_input("hello world 123") is True
    
    def test_validate_input_empty_string(self):
        """Test validation with empty string."""
        assert validate_input("") is False
    
    def test_validate_input_whitespace_only(self):
        """Test validation with whitespace only."""
        assert validate_input("   ") is False
    
    def test_validate_input_special_characters(self):
        """Test validation with special characters."""
        assert validate_input("hello@world") is False
    
    def test_validate_input_none(self):
        """Test validation with None input."""
        assert validate_input(None) is False
    
    def test_validate_input_non_string(self):
        """Test validation with non-string input."""
        assert validate_input(123) is False
