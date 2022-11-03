from abc import ABC, abstractmethod


class userDb(ABC):


    @abstractmethod
    def get_name(self):

        pass

    @abstractmethod
    def set_name(self, name):

        pass

    @abstractmethod
    def set_address(self, address):

        pass

    @abstractmethod
    def get_address(self):

        pass

    @abstractmethod
    def set_phonenumber(self, number):

        pass

    @abstractmethod
    def get_phonenumber(self):

        pass

    @abstractmethod
    def set_Id(self, ID):
        pass

    @abstractmethod
    def get_Id(self):

        pass
