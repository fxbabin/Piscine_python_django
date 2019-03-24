#!/bin/sh
curl $1 2> /dev/random | grep href | cut -d'"' -f2
