import subprocess


def instrument(target: str):
    subprocess.run(['afl-cc', '-o', 'instrumented_' + target, target])
