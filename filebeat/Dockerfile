FROM cr.yandex/yc-marketplace/yandex-cloud/filebeat-oss/filebeat-oss:7.12.1

COPY filebeat.yml /usr/share/filebeat/filebeat.yml
USER root
RUN chown -R root /usr/share/filebeat/
RUN chmod -R go-w /usr/share/filebeat/