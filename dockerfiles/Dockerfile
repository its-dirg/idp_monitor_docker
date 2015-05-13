FROM itsdirg/dirg_base

MAINTAINER DIRG <dirg@its.umu.se>

VOLUME ["/opt/idp_monitor/etc"]

RUN mkdir /opt/idp_monitor/src

ADD requirements.txt /opt/idp_monitor/requirements.txt

RUN apt-get update
RUN apt-get install -y --no-install-recommends\
        libsasl2-dev \
        libldap2-dev \
        libssl-dev \
        xmlsec1 \
        python-bs4 \
        python-mechanize
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r /opt/idp_monitor/requirements.txt

RUN git clone https://github.com/its-dirg/idp_monitor /opt/idp_monitor/src/idp_monitor

ADD start.sh /start.sh

WORKDIR /

CMD ["bash", "/start.sh"]
