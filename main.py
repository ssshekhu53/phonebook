from store.phonebook import Phonebook as pbStore
from service.phonebook import Phonebook as pbService
from execptions.phonebook import MissingParams, AlreadyExists, DoesNotExists, InvalidCommandParams
from constants.constants import FIRSTNAME, LASTNAME, PHONE

class Driver:
    def __init__(self, pbSvc):
        self.pbSvc = pbSvc

    def register(self, command):
        try:
            if len(command) != 3:
                raise InvalidCommandParams([FIRSTNAME, LASTNAME, PHONE])
            
            self.pbSvc.Register(*command)

            print("registered successfully")
        except (MissingParams, AlreadyExists) as e:
            print(e)
        except InvalidCommandParams as e:
            raise e
        except Exception as e:
            print("failed to register: ", e)

    def search(self, command):
        try:
            if len(command) != 2:
                raise InvalidCommandParams([f'search parameter ({FIRSTNAME, LASTNAME, PHONE})', 'search phrase'])
        
            users = self.pbSvc.Search(*command)
            if users == None or len(users) == 0:
                print("no user found")

                return
            
            for user in users:
                print(user)
        except InvalidCommandParams as e:
            raise e
        except Exception as e:
            print("failed to search: ", e)

    def update(self, command):
        try:
            if len(command) != 3:
                raise InvalidCommandParams([FIRSTNAME, f'update parameter ({LASTNAME, PHONE})', 'update value'])
            
            self.pbSvc.Update(*command)
            
            print(f"{command[1]} updated successfully")
        except DoesNotExists as e:
            print(e)
        except InvalidCommandParams as e:
            raise e
        except Exception as e:
            print("failed to update: ", e)

    def delete(self, command):
        try:
            if len(command) != 1:
                raise InvalidCommandParams(FIRSTNAME)
            
            self.pbSvc.Delete(*command)
            
            print("deleted successfully")
        except DoesNotExists as e:
            print(e)
        except InvalidCommandParams as e:
            raise e
        except Exception as e:
            print("failed to delete: ", e)


if __name__ == '__main__':
    pbStr = pbStore()
    pbSvc = pbService(pbStr)
    driver = Driver(pbSvc)

    commands = {
        "register": driver.register,
        "search": driver.search,
        "update": driver.update,
        "delete": driver.delete,
        "exit": quit,
    }

    while True:
        command = input().split()

        if len(command) == 0:
            print("invalid command!")
            
            continue

        if command[0] not in commands:
            print("invalid command")

            continue

        f = commands[command[0]]

        try:
            if command[0] == 'exit':
                f(0)

            f(command[1:])

            print()
        except Exception as e:
            print(e)