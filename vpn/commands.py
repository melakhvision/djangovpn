from subprocess import Popen, PIPE


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


def createClientProfile(name):
    command = [
        "cd /root",
        ""
        "source vars",
        f'./build-key {name}',
        f'cd keys'
    ]
