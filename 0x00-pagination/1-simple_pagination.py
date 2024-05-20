#!/usr/bin/env python3
""" task 1 answer """
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for pagination.

    Args:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

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
        """
        Takes 2 integer arguments and returns the requested page from the dataset.
        
        Args:
            page (int): The required page number. Must be a positive integer.
            page_size (int): The number of records per page. Must be a positive integer.
        
        Returns:
            List[List]: A list of lists containing the required data from the dataset.
        """
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        
        # Handle the case where the start index is beyond the dataset length
        if start_index >= len(dataset):
            return []
        
        return dataset[start_index:end_index]
