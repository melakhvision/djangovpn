#!/bin/bash

# Connect to the management interface, get the status, and then quit
status=$( (
    echo "status"
    sleep 3
    echo "quit"
) | nc localhost 7505)

# Extract the client list and convert it to JSON
clients=$(echo "$status" | awk '/CLIENT LIST/,/ROUTING TABLE/' | sed '1d;2d;3d;$d' | awk -v OFS=',' 'NF{NF--; print}' | awk -F',' '{printf "{\"Common Name\":\"%s\", \"Real Address\":\"%s\", \"Bytes Received\":\"%s\", \"Bytes Sent\":\"%s\", \"Connected Since\":\"%s\"},", $1, $2, $3, $4, $5}')

# Remove the trailing comma and wrap the client list in square brackets
clients="[$(echo $clients | sed 's/,$//')]"

# Extract the routing table and convert it to JSON
routing=$(echo "$status" | awk '/ROUTING TABLE/,/GLOBAL STATS/' | sed '1d;2d;$d' | awk -v OFS=',' 'NF{NF--; print}' | awk -F',' '{printf "{\"Virtual Address\":\"%s\", \"Common Name\":\"%s\", \"Real Address\":\"%s\", \"Last Ref\":\"%s\"},", $1, $2, $3, $4}')

# Remove the trailing comma and wrap the routing table in square brackets
routing="[$(echo $routing | sed 's/,$//')]"

# Convert the client list and routing table to JSON objects
clients_json=$(echo "$clients" | jq -c .)
routing_json=$(echo "$routing" | jq -c .)

# Combine the client list and routing table into a single JSON object
combined_json=$(echo "{\"clients\": $clients_json, \"routing\": $routing_json}" | jq -c .)

echo "$combined_json"
