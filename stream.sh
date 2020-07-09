#!/bin/bash -x

STREAM_KEY="" # Stream key from youtube
IP_CAM="rtsp://username:password@ip:554/11" # Camera RTSP URL for your camera

ffmpeg -f lavfi -i anullsrc -rtsp_transport udp -i $IP_CAM -tune zerolatency -vcodec libx264 -t 12:00:00 -s 640:480 -pix_fmt + -c:v copy -c:a aac -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/$STREAM_KEY
