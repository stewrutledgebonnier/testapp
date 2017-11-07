FROM python:3

ADD runit.py /

LABEL summary="$SUMMARY" \
      io.openshift.expose-services="8000:http" \
      io.openshift.tags="builder,python"
EXPOSE 8000
CMD [ "python", "runit.py" ]