from django.core.management.base import BaseCommand
from django.core.cache import cache
from subprocess import Popen, PIPE
from vpn.script.function import enable_scripts
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


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


# def enable_scripts():
#     command = [
#         f"chmod +x {BASE_DIR}/vpn/script/*.sh",
#     ]
#     result, err = processBaseCommand(command, join=True)
#     if err:
#         return err
#     return result


class Command(BaseCommand):
    help = 'Enable scripts'

    def handle(self, *args, **kwargs):
        result, err = enable_scripts()
        if err:
            self.stdout.write(self.style.ERROR('error please check the logs'))
        else:
            self.stdout.write(self.style.SUCCESS('script has been enabled'))
