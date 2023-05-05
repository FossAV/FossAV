#!/bin/bash
# compares program signatures

if [[ $# < 2 ]]
then
  echo "ERR: Invalid argument count. ($#)"
  echo "./compsig.sh <file> <hash>"
  exit
fi

PROG=$1
SIG=$2

PROG_SIG=$(sha256sum $1)

if [[ "$PROG_SIG" = "$SIG" ]]
then
  echo "Program signature matches provided signature."
else
  echo "Program signature does not match provided signature."
fi
