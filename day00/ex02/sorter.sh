#!/bin/bash

(head -n 1 ../ex01/hh.csv; \
 tail -n +2 ../ex01/hh.csv \
 | sort -t',' --key=2,2 --key=1,2) \
 > hh_sorted.csv