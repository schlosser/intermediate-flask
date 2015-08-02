Blask
=====

A blog in Flask.
## Running Blask

```
mongod &
virtualenv --no-site-packages .
source bin/activate
pip install -r requirements.txt
python reset_db.py         # Optional: wipe the databse
python run.py
```