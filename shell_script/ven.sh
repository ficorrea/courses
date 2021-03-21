#!/bin/bash

echo "Arquivo:"
read nome

virtualenv ${nome} -p /usr/bin/python3.5
