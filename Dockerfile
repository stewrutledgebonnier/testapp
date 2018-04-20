FROM python:3

ADD runit.py /

EXPOSE 8000

CMD [ "python", "-u", "runit.py" ]

