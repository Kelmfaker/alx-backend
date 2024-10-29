#!/usr/bin/env python3

"""
Function returns a tuple of size
"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes for pagination.

    Args:
    page (int): The current page number (1-indexed).
    age_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index and the end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
