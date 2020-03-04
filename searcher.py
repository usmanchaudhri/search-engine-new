from abc import ABC, abstractmethod
from indexer import Indexer

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class SearchService(ABC):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'search_by_id') and
                callable(subclass.search_by_id) and
                hasattr(subclass, 'search_by_query') and
                callable(subclass.search_by_query) or
                NotImplemented)

    def __init__(self):
        self.indexer = Indexer()

    @abstractmethod
    def search_by_query(self):
        raise NotImplementedError

class UsersSearchService(SearchService):
    def __init__(self, data: pd.DataFrame):
        self.user: pd.DataFrame = data

    def search_by_query(self, query: str):
        return self.user.query(query)

class TicketsSearchService(SearchService):
    def __init__(self, data: pd.DataFrame):
        self.tickets = data

    def search_by_query(self, query: str):
        return self.tickets.query(query)

class OrganizationSearchService(SearchService):
    def __init__(self, data: pd.DataFrame):
        self.organization = data

    def search_by_query(self, query: str):
        return self.organization.query(query)
