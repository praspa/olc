#!/bin/bash

oc delete template httpd-example -n olc 
oc delete all --all -n olc
