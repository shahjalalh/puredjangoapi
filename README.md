# Pure Django API

Python 3 virtual environment:
```
$ virtualenv -p /usr/bin/python3 py3env
$ source py3env/bin/activate
(py3env) $ pip install django==1.11.9
```

### User credentials:
```
user: shahjalal
pass: admin1234
```

1. Create (POST)
2. Retrieve (GET)
3. Update (PUT)
4. Delete (DELETE)

### The endpoints and the URLS

```
api/userprofiles/ GETs list of user profile
api/userprofiles/<id>/ GETs data of a specific user profile

api/userprofiles/create/ POST new user

```