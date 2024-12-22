#!/bin/bash

WEBSITE_URL=$1

receipient="techtinking@gmail.com"
sender="saurabhkumarsingh646@gmail.com"
subject="Website is not working"
message="The application is in terminated state."

check_website() {
    status_code=$(curl --head -s $WEBSITE_URL | awk '/^HTTP/{print $2}')
    if [[ $status_code == "200" || $status_code == "301" ]]; then
        echo "Website is up and running"
    else
        echo "Website is Down"
    fi
}

check_website