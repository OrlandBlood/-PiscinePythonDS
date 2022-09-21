#! /bin/bash
. oblood/bin/activate
pip3 install termgraph > /dev/null 2> /dev/null
termgraph data.dat --color {blue,magenta} --width 90
