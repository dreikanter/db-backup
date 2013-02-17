#!/usr/bin/env python
# coding: utf-8

"""Shared music backup tool"""

import argparse
from datetime import datetime
import glob
import logging
import os.path
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description='shared music backup tool')
    parser.add_argument('source',
                        metavar='<source/path>',
                        type=str,
                        help='source Shared Music dir location; env vars are allowed')
    parser.add_argument('dest',
                        metavar='<backup/path>',
                        type=str,
                        help='backup path; year/month-based dir structure could be used')
    parser.add_argument('-d', '--dry',
                        action='store_true',
                        help='dry run')
    args = parser.parse_args()
    return args.source, args.dest, args.dry


log_file = os.path.join(os.path.dirname(__file__), 'smbackup.log')
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s",
                              "%Y/%m/%d %H:%M:%S")
for ch in [logging.StreamHandler(), logging.FileHandler(log_file)]:
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    log.addHandler(ch)


source_path, backup_path, dryrun = parse_args()

if not os.path.isdir(source_path):
    log.error("source path not exists or not accessible: '%s'" % source_path)
    exit()

log.info('source path: ' + source_path)
log.info('backup path: ' + backup_path)
if dryrun:
    log.info('dry run mode enabled')

for file_name in glob.glob(os.path.join(source_path, '*')):
    if os.path.isdir(file_name):
        album_name = os.path.basename(file_name)
        album_date = datetime.fromtimestamp(os.path.getctime(file_name))
        date_path = album_date.strftime(backup_path)
        dest_path = os.path.join(date_path, album_name)

        if os.path.exists(dest_path):
            log.info(" - skipping '%s'" % album_name)
            continue

        log.info(" - copying '%s' to '%s'..." % (album_name, date_path))

        if dryrun:
            continue

        try:
            shutil.copytree(file_name, dest_path)
        except Exception as e:
            log.error(str(e))

log.info('done')
