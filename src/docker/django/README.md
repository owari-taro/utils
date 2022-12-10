
#
pipenv requirements --exclude-markers >requirements.txt


#
docker build -t dj .
docker run --rm dj python manage.py example --help