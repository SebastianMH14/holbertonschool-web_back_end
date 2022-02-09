#!/usr/bin/env python3
"""Implement a method named get_page that takes
two integer arguments page with default value 1
and page_size with default value 10."""
import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments page
        with default value 1 and page_size
        with default value 10"""
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)
        index = index_range(page, page_size)
        pages = self.dataset()
        if (index[0] > len(pages)):
            return []
        return pages[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing the following key-value pairs"""
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        next_page = page + 1
        prev_page = page - 1

        if (page > len(data)):
            next_page = None

        if (page <= 1):
            prev_page = None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
