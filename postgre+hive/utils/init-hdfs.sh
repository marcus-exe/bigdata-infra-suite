#!/bin/bash

echo "Checking if NameNode is already formatted..."

NAMENODE_DIR=/hadoop/dfs/name

# Step 1: Format only if not already formatted
if [ -d "$NAMENODE_DIR/current" ]; then
  echo "NameNode already formatted. Skipping format step."
else
  echo "Formatting NameNode..."
  hdfs namenode -format -force -nonInteractive
fi

echo "Starting HDFS directory initialization..."

# Step 2: Wait until NameNode is up
echo "Waiting for NameNode to be available..."
until hdfs dfsadmin -report > /dev/null 2>&1; do
  sleep 2
done

# Step 3: Create Hive directories
echo "Creating required HDFS directories..."

hadoop fs -mkdir -p /tmp
hadoop fs -chmod 1777 /tmp

hdfs dfs -mkdir -p /user/hive/warehouse
hdfs dfs -chmod -R 777 /user/hive/warehouse

echo "HDFS initialization complete."
