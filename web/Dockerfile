FROM cloudcourseproject_base

ENV APP_HOME /usr/src/app

COPY static/ \
     templates/ \
     app.py \
     requirements.txt \
     ${APP_HOME}/

WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

RUN touch /var/log/spa.log