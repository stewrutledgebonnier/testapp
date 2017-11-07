FROM python:3

ADD runit.py /

LABEL summary="$SUMMARY" \
      io.openshift.expose-services="8000:http" \
      io.openshift.tags="builder,python" \

CMD [ "python", "runit.py" ]