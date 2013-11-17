
import os


def find_public_ssh_keys(dir):
    for (dirpath, dirnames, filenames) in os.walk(dir):
        for filename in filenames:
            if filename.endswith('_rsa.pub') or filename.endswith('_dsa.pub'):
                yield os.path.join(dirpath, filename)
