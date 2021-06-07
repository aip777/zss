### Setup
    Download the files from this repo

    Change the directory to the folder where you downloaded files

    For installing required packages, execute the following command in terminal:

    pip install -r requirements.txt

    After successful installation execute the following commands:

    python manage.py migrate
    python manage.py runserver

### Admin
    Country List
    http://127.0.0.1:8000/

    Add country
    http://127.0.0.1:8000/add-country/

    State List
    http://127.0.0.1:8000/state-list/

    Add State
    http://127.0.0.1:8000/add-state/

    Address List
    http://127.0.0.1:8000/address-list/

    Add Address
    http://127.0.0.1:8000/add-address/


### Country API

    Filter countries by name
    http://127.0.0.1:8000/api/country/?country=india

    Filter countries by code
    http://127.0.0.1:8000/api/country/?code=BD

    Country List
    http://127.0.0.1:8000/api/country/

    Create Country
    http://127.0.0.1:8000/api/country/

    Request:
            {
            "name": "Bangladesh",
            "latitude": 2322312312,
            "longitude": 121212132
            }

    Country Update
    http://127.0.0.1:8000/api/country/2/

    Request:
            {
            "id": 2,
            "name": "Egypt",
            "latitude": 15211.0,
            "longitude": 45210.0,
            "code": "EG"
            }

    Country Delete
    http://127.0.0.1:8000/api/country/2/

    
### State API
    List all states by countries
    http://127.0.0.1:8000/api/state/?country=india

    Filter states by name
    http://127.0.0.1:8000/api/state/?state=dhaka

    State List
    http://127.0.0.1:8000/api/state/

    Create State
    http://127.0.0.1:8000/api/state/

    Request:
            {
                "name": "Dhaka",
                "country": 5
            }

    State Update
    http://127.0.0.1:8000/api/state/4/

    Request:
            {
                "id": 4,
                "name": "Sylhet",
                "country": 5
            }

    State Delete
    http://127.0.0.1:8000/api/state/4/

### Address API
    List addresses of states.

    http://127.0.0.1:8000/api/address/?state=dhaka

    Filter addresses by house_number
    http://127.0.0.1:8000/api/address/?house=212

    Filter addresses by road_number
    http://127.0.0.1:8000/api/address/?road=11

    Address List
    http://127.0.0.1:8000/api/address/

    Create Address
    http://127.0.0.1:8000/api/address/

    Request:
            {
                "name": "Darjeeling",
                "state": 6,
                "house_number": "23",
                "road_number": 32
            }

    Address Update
    http://127.0.0.1:8000/api/address/6/

    Request:
            {
                "id": 6,
                "name": "Darjeeling Manibangong",
                "state": 6,
                "house_number": "23",
                "road_number": 32
            }

    Address Delete
    http://127.0.0.1:8000/api/address/6/

### Login and Registration API
    Login:

    http://127.0.0.1:8000/account/login-api/

    POST request: 
        data = {
        "email":"admin@admin.com",
        "password":"admin"
        }
    
    Registration:
    http://127.0.0.1:8000/account/register/

    POST Request:
        data = {
        "username":"emarn6",
        "email":"emarn6@admin.com",
        "password":"admin123"
        }