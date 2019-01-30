#!/bin/bash
video=$1
ip="192.168.1.219"
name="root"

./annotation.exp $name $ip $video

#---------------------------------------------------------------------------

date_time=`date "+%Y%m%d"`
xml_dir=$date_time"_xml"
image_dir=$date_time"_image"
background_dir=$date_time"_background"
mkdir -p $xml_dir
mkdir -p $image_dir
mkdir -p $background_dir

./rsync_xml_and_image_fit_server.exp $date_time $xml_dir $image_dir $background_dir



