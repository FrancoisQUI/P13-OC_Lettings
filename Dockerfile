FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ARG SECRET_KEY
ARG ALLOWED_HOSTS=[]
ARG DEBUG=True
ARG PORT=8000

ENV SECRET_KEY=$SECRET_KEY
ENV ALLOWED_HOSTS=$ALLOWED_HOSTS
ENV PORT=$PORT
ENV DEBUG=$DEBUG

COPY . .

EXPOSE $PORT

CMD [ "python","manage.py","runserver" ]