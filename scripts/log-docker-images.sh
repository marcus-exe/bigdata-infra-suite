#!/bin/bash

# Check if a directory path was passed
if [[ -z "$1" ]]; then
  echo "Usage: $0 <path-to-projects>"
  exit 1
fi

# Use provided path
ROOT_DIR="$1"

# Check if the provided path is valid
if [[ ! -d "$ROOT_DIR" ]]; then
  echo "❌ Provided path '$ROOT_DIR' is not a valid directory."
  exit 1
fi

# Script directory (for saving logs)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Output log file
LOG_FILE="$SCRIPT_DIR/docker-service-logs.log"
> "$LOG_FILE"  # Clear previous log

# Find all docker-compose files in the given path
COMPOSE_FILES=$(find "$ROOT_DIR" -maxdepth 2 -type f \( -name "docker-compose.yml" -o -name "docker-compose.yaml" \))

if [[ -z "$COMPOSE_FILES" ]]; then
  echo "❌ No docker-compose files found under $ROOT_DIR"
  exit 1
fi

# Loop through each compose file
for COMPOSE_FILE in $COMPOSE_FILES; do
  PROJECT_DIR=$(dirname "$COMPOSE_FILE")
  PROJECT_NAME=$(basename "$PROJECT_DIR")

  echo "📦 Project: $PROJECT_NAME" >> "$LOG_FILE"
  echo "Compose File: $COMPOSE_FILE" >> "$LOG_FILE"
  echo "Timestamp: $(date)" >> "$LOG_FILE"
  echo "-------------------" >> "$LOG_FILE"

  # Extract container names
  CONTAINER_NAMES=$(grep 'container_name:' "$COMPOSE_FILE" | awk '{print $2}')

  if [[ -z "$CONTAINER_NAMES" ]]; then
    echo "❌ No container names found in $COMPOSE_FILE" >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
    continue
  fi

  for CONTAINER in $CONTAINER_NAMES; do
    echo "- $CONTAINER" >> "$LOG_FILE"
  done

  echo -e "\n===============================\n" >> "$LOG_FILE"

  # Get logs
  for CONTAINER in $CONTAINER_NAMES; do
    echo "🔹 Logs for $CONTAINER:" >> "$LOG_FILE"
    docker logs "$CONTAINER" >> "$LOG_FILE" 2>&1
    echo -e "\n-------------------------------\n" >> "$LOG_FILE"
  done

  echo -e "\n\n" >> "$LOG_FILE"
done

echo "✅ Docker logs saved to $LOG_FILE"
