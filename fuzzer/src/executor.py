import subprocess
import time


def execute(target: str):
    start_time = time.time()
    process = subprocess.Popen(['./' + target], stdout=subprocess.PIPE)
    process.wait()
    end_time = time.time()
    return end_time - start_time
