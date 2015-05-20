.. _configuration:

*************************
Idp monitor configuration
*************************

Setting up idp monitor docker container

Docker volume structure
=======================

To run the idp monitor, you need to bind a volume to **/opt/idp_monitor/etc** in the container.
This volume need to hold all configurations of the idp monitor.

An example of how to build a valid volume to the container can be found in the **example/etc** directory.
And how to bind the volume can be found in the **example/run.sh** script.

The start.sh script
-------------------

In the volume root, a file named **start.sh** must exist. This file is the starting point of the application and is
responsible of starting the idp monitor.

An example of a start script::

    #!/bin/bash

    python idp_monitor.py conf

This starts the idp monitor with the config file **conf.py**.
