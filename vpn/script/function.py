# get the current path using os
import os
from core.settings import BASE_DIR, MEDIA_PATH
from subprocess import Popen, PIPE
import subprocess


print(BASE_DIR)


def processBaseCommand(command, join=False):
    if join:
        command = ' && '.join(command)
        process = subprocess.run(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            return process.stdout.decode(), process.stderr.decode()
        return process.stdout.decode(), None


def list_dir():
    command = [
        f"cd {BASE_DIR}/vpn/script",
        'ls -l'
    ]
    result = processBaseCommand(command, join=True)
    return result


def create_profile(name):
    print(f"the name of the profile is {name}")
    command = [
        f"cd {BASE_DIR}/vpn/script && ./create.sh {name}"
    ]
    result, err = processBaseCommand(command, join=True)
    if err:
        print(f"an error occured : {err}")
        return err
    return None


def revoke_profile(name):
    command = [
        f"cd {BASE_DIR}/vpn/script && ./remove.sh {name}"

    ]
    result, err = processBaseCommand(command, join=True)
    if err:
        return err
    return result.encode()


def enable_scripts():
    command = [
        f"chmod +x {BASE_DIR}/vpn/script/*.sh",
    ]
    return processBaseCommand(command, join=True)


def ban_ip(ip):
    command = [
        f"sudo ufw insert 1 deny from {ip} to any port 80"
    ]
    result, err = processBaseCommand(command, join=True)
    if err:
        return err
    return result
