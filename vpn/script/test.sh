#!/usr/bin/expect
# folderName=$1
# Define the answers for the first two questions
# set folderName [lindex $argv 0]

# mkdir $folderName
set actionIndex [lindex $argv 0]
set profileName [lindex $argv 1]

echo "action is $actionIndex and profile is $profileName"
