find . -path "/find_your_buddy/fyb_web/migrations/*.py" -not -name "__init__.py" -delete; #deletes all of the .py files in the migrations directory except for the __init__.py file.
find . -path "/find_your_buddy/fyb_web/migrations/*.pyc"  -delete; #deletes all of the .pyc files in the migrations directory.
rm db.sqlite3; #deletes the database file.
rm -rf fyb_web/migrations; #deletes the migrations folder.
python manage.py migrate; #run the initial django migration to create all the initial tables. need this step because we are killing the database just above
python manage.py makemigrations fyb_web; #creates the migration.
python manage.py migrate fyb_web; #runs the migration.  This will delete all of the data in your database.
# python manage.py loaddata user.json  #loads the data from each .json file in sequential order.