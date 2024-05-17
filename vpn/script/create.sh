#!/usr/bin/expect

# Define the answers for the first two questions
set actionIndex [lindex $argv 0]
set profileName [lindex $argv 1]

# Start the script
spawn /root/openvpn-install.sh
# Expect the first question and send the answer
expect "What do you want to do?"
send "$actionIndex\r"

# Expect the second question and send the answer
expect "Tell me a name for the client"
send "$profileName\r"

# Expect the third question and send Enter
expect "*third parameter:*"
send "\r"

# Wait for the script to finish
expect eof
