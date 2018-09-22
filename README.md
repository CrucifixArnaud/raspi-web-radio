# Raspi Web Radio

A small raspberry web radio controller for mpd (https://www.musicpd.org/).

## Edit radio list

sudo vim /var/lib/mpd/playlists/radio.m3u
mpc clear
mpc load radio
