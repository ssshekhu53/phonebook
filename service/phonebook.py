from model.phonebook import Phonebook as modelPb
from store.phonebook import Phonebook as storePb
from execptions.phonebook import MissingParams, AlreadyExists, DoesNotExists
from constants.constants import LASTNAME, PHONE

class Phonebook:
    def __init__(self, store):
        self.store = store

    def Register(self, firstName, lastName, phone):
        err = Phonebook.validate(firstName, lastName, phone)
        if err != None:
            raise err
        
        if self.store.GetByFirstName(firstName) != None:
            raise AlreadyExists(firstName)
        
        self.store.Register(firstName, lastName, phone)

    def Search(self, searchKey, searchPhrase):
        return self.store.Search(searchKey, searchPhrase)

    def Update(self, firstname, updateKey, updateValue):
        user = self.store.GetByFirstName(firstname)

        if user == None:
            raise DoesNotExists
        
        if updateKey == LASTNAME:
            user.LastName = updateValue
        elif updateKey == PHONE:
            user.Phone = updateValue

        self.store.Update(user.FirstName, user)

    def Delete(self, firstname):
        user = self.store.GetByFirstName(firstname)

        if user == None:
            raise DoesNotExists
        
        self.store.Delete(firstname)     


    @staticmethod
    def validate(firstName, lastName, phone):
        params = []

        if firstName == '':
            params.append('firstName')
        
        if lastName == '':
            params.append('lastName')

        if phone == '':
            params.append('phone')

        if len(params) == 0:
            return None
        
        return MissingParams(params)

