from ubuntu:18.04

RUN apt-get update && apt-get install -y syslog-ng && mkdir -p /app

COPY rate_limit_test.conf /etc/syslog-ng/syslog-ng.conf
COPY rate_limiter.py /usr/local/bin/rate_limiter.py

RUN chmod +x /usr/local/bin/rate_limiter.py

CMD ["syslog-ng", "-F", "-f", "/etc/syslog-ng/syslog-ng.conf"]