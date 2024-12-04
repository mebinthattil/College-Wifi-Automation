#!/bin/zsh

while true; do
  python3 main.py
  echo "Last run --> $(DATE)"
  sleep 120
done
