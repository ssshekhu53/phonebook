from store.phonebook import Phonebook as pbStore
from service.phonebook import Phonebook as pbService

pbStr = pbStore()
pbSvc = pbService(pbStr)

pbSvc.Register("ll", "ff", "999")
pbSvc.Register("ll3", "ff", "999")

print(pbSvc.Search("lastname", "f"))