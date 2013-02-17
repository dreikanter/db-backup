@echo off
rem Script scheduling example for windows: runs backup each sunday at 23:00.
rem This script should be executed under admin account.
at 23:00 /every:Su "D:\src\dotfiles\bin\smbackup.bat"
