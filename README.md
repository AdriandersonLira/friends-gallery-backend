# friends-gallery-backend

-Commands
```
$ pip install flask-restx
$ pip install typing-extensions
$ pip install pymongo
$ pip install jwt
$ python -c 'import os; print(os.urandom(16))'
$ export FLASK_APP=main.py
$ pip install -r requirements.txt
$ python -m flask run or $ python main.py
```

[x] user
  - get 
    - get user by id
  - post 
    - create user
      {
        "nickname": str,
        "email": str,
        "password": str,
      }
  -put
    - update user by id
      {
        "id": _id,
        "nickname": str,
        "email": str,
        "password": str,
      }

[x] session
  - post 
    - create session
      {
        "nickname": str,
        "email": str,
        "password": str,
      }

[ ] moment
  - get 
    - get moments by idAdmin

  - post 
    - create moment
      {
        "idMoment": _id
        "idUser": _id,
        "idAdmin": _id,
        "picture": filename,
        "likes": int,
        "approved": null or boolean,
        "comments": {
          "idUser": _id,
          "comment": str,
        },
      }

    - delete moment


[ ] gallery
  - get gallery

  - post 
    - create gallery
      {
        "idGallery": _id
        "nameGallery": str
        "admins": max 2 {"idsUsers"},
        "moments": {"idsMoments"}
        "password": str,
      }

  - update gallery

  - delete gallery