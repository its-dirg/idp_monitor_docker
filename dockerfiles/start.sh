#!/bin/bash

volumePath=/opt/idp_monitor/etc/
src=/opt/idp_monitor/src/idp_monitor/

linkFiles() {

    ALL_FILES=$(ls -1 ${volumePath}${1})

    for file in ${ALL_FILES}
    do
        if [ ${2} ]; then
            rm -fr ${src}${1}/${file} > /dev/null 2> /dev/null
        fi
        ln -s ${volumePath}${1}/${file} ${src}${1}/${file}
    done

}

linkFiles . 1

cd ${src}

./start.sh
