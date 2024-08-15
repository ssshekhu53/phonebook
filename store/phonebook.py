from model import Phonebook as modelPhonebook
from constants import FIRSTNAME, LASTNAME, PHONE

class Phonebook:
    def New(self):
        self.Directory = {}

    def Register(self, firstName, lastName, phone):
        self.Directory[firstName] = modelPhonebook.New(firstName, lastName, phone)

    def Search(self, searchKey, searchValue):
        if searchKey == FIRSTNAME:
            return self.searchByFirstName(searchValue)
        elif searchKey == LASTNAME:
            return

    def Update(self, firstName, phonebook):
        self.Directory[firstName] = phonebook

    def Delete(self, firstName):
        del(self.Directory[firstName])

    def searchByFirstName(self, firstName):
        users = []

        for value in self.Directory.values():
            if value.FirstName.startswith(firstName):
                users.append(value.FirstName)
        
        return users
    
    def searchByLastName(self, lastName):
        users = []

        for value in self.Directory.values():
            if value.LastName.startswith(lastName):
                users.append(value.FirstName)
        
        return users
    
    def searchByPhone(self, phone):
        users = []

        for value in self.Directory.values():
            if value.Phone.startswith(phone):
                users.append(value.FirstName)
        
        return users