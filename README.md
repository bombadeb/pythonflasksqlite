# pythonflasksqlite
Sample API for learning DB insertion, get and update

### Setup up virtual environment
```sh
virtualenv env
pip install flask flask-alchemy
```

### Setup up DB
```sh
python 
>> from app import db
>> db.create_all()
```

### Running app
```sh
python .\app.py
```
