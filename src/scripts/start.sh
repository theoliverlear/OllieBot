#!/bin/bash
source /home/ludwig/GitHub/OllieBot/environment/bin/activate
export PYTHONPATH="/home/ludwig/GitHub/OllieBot"
echo "Starting OllieBot"
PYTHONPATH=$PYTHONPATH /home/ludwig/GitHub/OllieBot/environment/bin/python3 /home/ludwig/GitHub/OllieBot/src/main/main.py
echo "OllieBot has stopped"