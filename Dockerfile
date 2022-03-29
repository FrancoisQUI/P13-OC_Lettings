FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV SECRET_KEY=fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s

COPY . .
RUN python manage.py collectstatic


EXPOSE 8000

CMD [ "gunicorn", "oc_lettings_site.wsgi" ]