#!/bin/bash

mkdir -p build
mkdir -p compile

make clean
make
./compile/my_program