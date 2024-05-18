# get the current path using os
import os
from core.settings import BASE_DIR, MEDIA_PATH
from subprocess import Popen, PIPE


print(BASE_DIR)


def processBaseCommand(command, join=False):
    if join:
        return Popen(
            "/bin/bash",
            shell=False,
            universal_newlines=True,
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        ).communicate("\n".join(command))
    else:
        return Popen(
            "/bin/bash",
            shell=False,
            universal_newlines=True,
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        ).communicate(command)


def list_dir():
    command = [
        f"cd {BASE_DIR}/vpn/script",
        'ls -l'
    ]
    result = processBaseCommand(command, join=True)
    return result


def create_profile(index, name):
    command = [
        f"cd {BASE_DIR}/vpn/script && ./create.sh {index} {name} && cp /root/{name}.ovpn {MEDIA_PATH}"
    ]
    result, err = processBaseCommand(command, join=True)
    if err:
        return err
    return result


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
