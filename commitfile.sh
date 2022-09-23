#!/bin/bash  
sudo python3 ./parser_obi.py
git add .  
git commit -a -m date
git push --force origin master