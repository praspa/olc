#!/bin/bash

oc create -f httpd-example.yaml -n olc 
oc new-app --template="olc/httpd-example" -p "NAME=chat"
