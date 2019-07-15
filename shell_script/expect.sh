#!/bin/bash
video=$1
startid=$2
video_=$3
ip="192.168.1.219"
name="root"

./annotation.exp $name $ip $video $startid $video_

#---------------------------------------------------------------------------

date_time=`date "+%Y%m%d"`
xml_dir=$date_time"_xml"
image_dir=$date_time"_image"
background_dir=$date_time"_background"
top_path="/data/darknet/python/"
mkdir -p $top_path$xml_dir
mkdir -p $top_path$image_dir
mkdir -p $top_path$background_dir

./rsync_xml_and_image_fit_server.exp $date_time $xml_dir $image_dir $background_dir


python3 /datasets/labelImg/labelImg.py $image_dir &



