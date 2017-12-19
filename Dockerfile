FROM python:3

ADD runit.py /
ADD tree.svg /

EXPOSE 8000

CMD [ "python", "-u", "runit.py" ]
