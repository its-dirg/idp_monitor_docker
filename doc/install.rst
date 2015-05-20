.. _install:

*******************
Quick install guide
*******************

Install Docker
==============

To install docker on your specific OS, follow the instruction on the docker page: http://docs.docker.com/installation/

Install idp monitor using docker
================================

Download the idp monitor docker project from: https://github.com/its-dirg/idp_monitor_docker

All files necessary to build the idp monitor image are located in the **dockerfiles** directory. To build the image run the script::

    dockerfiles/build.sh

If you want to test the idp monitor, you can use the example setup in the example directory and add your own metadata and key files.

To start the idp monitor run the script::

    example/run.sh

