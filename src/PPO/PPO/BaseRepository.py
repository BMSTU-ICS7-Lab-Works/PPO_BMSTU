from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def insert(self, obj):
        pass

    @abstractmethod
    def update(self, id, obj):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def select(self, id):
        pass