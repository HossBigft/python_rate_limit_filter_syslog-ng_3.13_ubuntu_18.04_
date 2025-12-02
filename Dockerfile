from ubuntu:18.04

ENV PYTHONPATH="/etc/syslog-ng/python"

RUN apt-get update && apt-get install -y syslog-ng  && apt install netcat -y && mkdir /etc/syslog-ng/python/

COPY rate_limit_test.conf /etc/syslog-ng/conf.d/rate_limit_test.conf
COPY rate_limiter.py /etc/syslog-ng/python/rate_limiter.py

RUN chmod +x /etc/syslog-ng/python/rate_limiter.py

CMD ["syslog-ng", "-F", "-f", "/etc/syslog-ng/syslog-ng.conf"]