FROM python:3.6.7-alpine


ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache build-base python3 python3-dev libffi-dev postgresql-dev linux-headers tzdata

# ENV TZ=Australia/Sydney

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./entrypoint.sh /
RUN ["chmod", "+x", "/entrypoint.sh"]
ADD ./ /app
WORKDIR /app

ENTRYPOINT [ "/entrypoint.sh" ]

EXPOSE 9000

