@echo off
rem smbackup usage example for windows environment
python %~dp0smbackup.py "%userprofile%\Desktop\Dropbox\Shared Music" "e:\mp3\dropbox-music\%%Y-%%m" %1
