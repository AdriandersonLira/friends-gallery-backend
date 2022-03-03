# friends-gallery-backend

-Commands
```
$ py -m venv venv

No Windows, execute:
$ cd ./venv/Scripts/activate.bat
No Unix ou no MacOS, executa:
$ source venv/bin/activate

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
        "idGallery": _id,
        "idUser": _id,
        "picture": filename,
        "likes": int,
        "approved": null or boolean,
        "comments": {
          "idUser": _id,
          "comment": str,
        },
      }

    - delete moment


[x] gallery
  - get gallery

  - post (apenas uma gallery por admin)
    - create gallery
      {
        "idGallery": _id
        "name": str
        "admins": max 2 {"idsUsers"},
        "moments": {"idsMoments"}
        "password": str,
      }

  - update gallery

  - delete gallery