# Django project that uses YouTubes APIs to retreive video data

cd to development directory

clone repository to new directory

pip install -r requirements.txt

Update settings.py with your youtube api

GOOGLE_API_KEY = "XXX"

CHANNEL_ID = 'XXX'

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
https://localhost:8000
