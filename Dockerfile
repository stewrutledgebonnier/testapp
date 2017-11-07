FROM python:3

ADD runit.py /

CMD [ "python", "runit.py" ]