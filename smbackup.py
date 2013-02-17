#!/usr/bin/env python
# coding: utf-8

"""Shared music backup tool"""

import argparse
from datetime import datetime
import glob
import os.path
import shutil


def makedirs(dir_path):
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
        return True
    return False


def parse_args():
    parser = argparse.ArgumentParser(description='shared music backup tool')
    parser.add_argument('source',
                        metavar='<source/path>',
                        type=str,
                        help='source Shared Music dir location; env vars are allowed; example: "$userprofile/Desktop/Dropbox/Shared Music"')
    parser.add_argument('dest',
                        metavar='<backup/path>',
                        type=str,
                        help='backup path; year/month-based dir structure could be used; example: "/backup/shared-music/%%Y-%%m"')
    parser.add_argument('-d', '--dry',
                        action='store_true',
                        help='dry run')
    args = parser.parse_args()
    return args.source, args.dest, args.dry


source_path, backup_path, dryrun = parse_args()

if not os.path.isdir(source_path):
    exit('source path not exists or accessible')

print('source path: ' + source_path)
print('backup path: ' + backup_path)
if dryrun:
    print('dry run mode enabled')

for file_name in glob.glob(os.path.join(source_path, '*')):
    if os.path.isdir(file_name):
        album_name = os.path.basename(file_name)
        album_date = datetime.fromtimestamp(os.path.getctime(file_name))
        date_path = album_date.strftime(backup_path)
        dest_path = os.path.join(date_path, album_name)

        if os.path.exists(dest_path):
            print(" - skipping '%s'" % album_name)
            continue

        print(" - copying '%s' to '%s'..." % (album_name, date_path))

        if dryrun:
            continue

        try:
            shutil.copytree(file_name, dest_path)
        except Exception as e:
            print e

print 'done'
