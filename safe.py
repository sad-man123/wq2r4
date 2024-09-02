import time
import os, url, shutil

while True:
    if os.path.isdir(f"{url.url}/test_dir"):
        time.sleep(1)
    else:
        shutil.copytree("test_dir", f"{url.url}/test_dir")
