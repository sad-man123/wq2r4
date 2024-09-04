import time
import os, url, shutil

num_1 = 0
while True:
    if os.path.isdir(f"{url.url}/server") and num_1 <= 3:
        time.sleep(1)
        num_1 += 1
    else:
        num_1 = 0
        shutil.copytree("server", f"{url.url}/server")
        os.startfile(f"{url.url}/server/safe.py")