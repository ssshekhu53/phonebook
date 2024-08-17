from model.phonebook import Phonebook as modelPhonebook
from constants.constants import FIRSTNAME, LASTNAME, PHONE

class Phonebook:
    def __init__(self):
        self.directory = {}

    def Register(self, firstName, lastName, phone):
        self.directory[firstName] = modelPhonebook(firstName, lastName, phone)

    def GetByFirstName(self, firstName):
        return self.directory.get(firstName)

    def Search(self, searchKey, searchPhrase):
        if searchKey == FIRSTNAME:
            return self.searchByFirstName(searchPhrase)
        elif searchKey == LASTNAME:
            return self.searchByLastName(searchPhrase)
        elif searchKey == PHONE:
            return self.searchByPhone(searchPhrase)

    def Update(self, firstName, phonebook):
        self.directory[firstName] = phonebook

    def Delete(self, firstName):
        del(self.directory[firstName])

    def searchByFirstName(self, firstName):
        users = []

        for value in self.directory.values():
            if value.FirstName.startswith(firstName):
                users.append(value.FirstName)
        
        return users
    
    def searchByLastName(self, lastName):
        users = []

        for value in self.directory.values():
            if value.LastName.startswith(lastName):
                users.append(value.FirstName)
        
        return users
    
    def searchByPhone(self, phone):
        users = []

        for value in self.directory.values():
            if value.Phone.startswith(phone):
                users.append(value.FirstName)
        
        return users