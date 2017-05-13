FROM cloudcourseproject_base

ENV APP_HOME /usr/src/app

COPY static/ \
     templates/ \
     app.py \
     requirements.txt \
     ${APP_HOME}/

WORKDIR ${APP_HOME}
RUN pip install --no-cache-dir -r requirements.txt

RUN touch /var/log/spa.log