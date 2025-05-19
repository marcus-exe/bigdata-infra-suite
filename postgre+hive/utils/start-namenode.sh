#!/bin/bash
# start-namenode.sh

/entrypoint.sh &

# Wait until the namenode RPC port (8020) is open
echo "Waiting for NameNode to be ready..."
until nc -z localhost 8020; do
  sleep 1
done

/init-hdfs.sh

wait
