Media management for streaming your goats from your IP camera to YouTube live using ffmpeg
==========================================================================================

Requirements
------------

* An IP camera with RTSP support
* ffmpeg
* A youtube live channel set up with a streaming key to use

Steps
-----

* Make a user: `adduser goatstream`
* Edit stream.sh to set your IP cam RTSP URL and YouTube streaming key
* Test ./stream.sh on its own and futz around with it until it can stream to YouTube
* Copy the systemd scripts to `/etc/systemd/system/`
* Copy the rest of the scripts to the goatstream user's home directory. Don't let the goatstream user edit them because they'll have sudo perms on them.
* You should be able to start and stop the stream with `sudo systemctl start goatstream`
* Add to sudoers: `goatstream ALL=(ALL) NOPASSWD: /home/goatstream/start.sh` and `goatstream ALL=(ALL) NOPASSWD: /home/goatstream/stop.sh`
* Make sure the goatstream user can to `sudo systemctl start goatstream` and `sudo systemctl start goatstream` without a password
* Start the goat management web UI with `sudo systemctl start goatmanager`
* You should now be able to start and stop the stream to youtube at `http://your_ip:8000`
