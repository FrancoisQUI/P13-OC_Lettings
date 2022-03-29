FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV SECRET_KEY=$SECRET_KEY
ENV ALLOWED_HOSTS=$ALLOWED_HOSTS
ENV PORT=$PORT

COPY . .
RUN python manage.py collectstatic


EXPOSE 8000

CMD [ "gunicorn", "oc_lettings_site.wsgi" ]