import json
import requests


url = "https://petstore.swagger.io/v2/pet"

PetType = input('Enter your pet type: ')
PetName = input('Entwr your pet name: ')

PostDict = {"id": 0,"category": {"id": 0,"name": PetType },
            "name": PetName, "photoUrls": ["string"],
            "tags": [ {"id": 0,"name": "string"} ],
            "status": "available"}

CreatePetReq = requests.post(url,json = PostDict)
print('Your pet was created with next parametrs: {}'.format(json.dumps(PostDict)))

#ViewPetReq = requests.get(url,PostDict("id"))

CreatePetRes = CreatePetReq.json()

petid = CreatePetRes['id']
petid = str(petid)

Question = input('Do you want delete your pet? Yes or No ')
if Question == 'Yes' or 'yes':
    DeletePetReq = requests.delete(url + petid)
    print ('Pet with name {} was deleted'.format(PetName))
else:
    GetPetReqByID = requests.get(url + petid)
    print(GetPetReqByID.text)