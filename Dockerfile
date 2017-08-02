FROM python:3.5-slim
RUN apt-get update && \
    apt-get -y install gcc
RUN mkdir -p /opt/apps
ENV APP_DIR /opt/apps/wordcount
ADD . $APP_DIR
WORKDIR $APP_DIR
RUN pip install -r requirements.txt
ADD docker_bins/* /usr/local/bin/
EXPOSE 5000
ENTRYPOINT ["entry"]
CMD ["app"]
