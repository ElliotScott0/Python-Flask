FROM python:3.9

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y supervisor

RUN pip install --upgrade pip
COPY requirements.txt /home/
RUN pip install -r /home/requirements.txt
RUN pip install mysql-connector-python
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:80 || exit 1
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /etc/supervisor/conf.d
COPY supervisor/*.conf /etc/supervisor/conf.d/
WORKDIR /app
COPY *.py ./
COPY templates/*.* ./templates/
EXPOSE 8080 80 5000
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]