import requests

# below 
#BASE_URL='http://127.0.0.1:8000/api/'

# below payload for all method for single record
BASE_URL='http://127.0.0.1:8000/api/3/'

# below payload for post,put,patch
payload={
    "name": "umar",
    "email": "hamza@gmail.com",
    "password": "mm123123"
}

#r=requests.get(BASE_URL)
#r=requests.post(BASE_URL,data=payload)
# r=requests.put(BASE_URL,data=payload)
# r=requests.patch(BASE_URL,data=payload)
r=requests.delete(BASE_URL)


if r.status_code==200:
    # GET 
    '''data=r.json()
    print()
    for d in data:
        print(d)
    '''
    # POST
    #print('record added into db')

    # PUT
    #print('record fully updated')


    # PATCH
    #print('record partially updated')

    # DELETE
    print('record deleted')

else:
    print(r.status_code)
