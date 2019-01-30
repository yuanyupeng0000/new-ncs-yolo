#!/bin/bash
video=$1
ip="192.168.1.219"
name="root"

./annotation.exp $name $ip $video
/data/darknet/python/rsync_xml_and_image_fit_server.sh

