# frf-music-backup

A backup script for friendfeed shared music community.

Command line options:

![help](screenshots/help.png)

Usage example for Windows environment:

```bat
python %~dp0smbackup.py "%userprofile%\Desktop\Dropbox\Shared Music" "e:\mp3\dropbox-music\%%Y-%%m" %1
```

Scheduling to run each sunday at 23:00:

```bat
at 23:00 /every:Su "D:\src\dotfiles\bin\smbackup.bat"
```

Sample run:

```
2013/02/17 14:04:27 INFO: source path: C:\Users\alex\Desktop\Dropbox\Shared Music
2013/02/17 14:04:27 INFO: backup path: e:\mp3\dropbox-music\%Y-%m
2013/02/17 14:04:27 INFO:  - copying 'Ametsub - All is Silence (2012)' to 'e:\mp3\dropbox-music\2013-02'...
2013/02/17 14:04:28 INFO:  - copying 'Apparat - Krieg Und Frieden (Music For Theatre) (2013)' to 'e:\mp3\dropbox-music\2013-02'...
2013/02/17 14:04:28 INFO:  - skipping 'Brian Tyler - Far Cry 3 (2012)'
2013/02/17 14:04:28 INFO:  - copying 'Cloud Cult - Love - 2013 (320 kbps)' to 'e:\mp3\dropbox-music\2013-02'...
2013/02/17 14:04:29 INFO:  - copying 'Grouper - The Man Who Died in His Boat (2013) - 320' to 'e:\mp3\dropbox-music\2013-02'...
2013/02/17 14:04:29 INFO:  - copying 'Ludovico Einaudi - In A Time Lapse (2013)' to 'e:\mp3\dropbox-music\2013-02'...
2013/02/17 14:04:29 INFO:  - skipping 'Mînikà Rîsñhår Âig Âànd - Fàilurå In Wîndårlànd (2012)'
2013/02/17 14:04:29 INFO:  - copying 'Nick Cave And The Bad Seeds-Push the Sky Away' to 'e:\mp3\dropbox-music\2013-02'...
2013/02/17 14:04:30 INFO:  - copying 'Zemfira 2012 To Live In Your Head' to 'e:\mp3\dropbox-music\2013-02'...
2013/02/17 14:04:31 INFO: done
```

Result:

![backup dir](screenshots/backup-dir.png)
