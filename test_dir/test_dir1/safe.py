import time
import os, url, shutil

num_1 = 0
while True:
    if os.path.isdir(f"{url.url}/test_dir") and num_1 <= 3:
        time.sleep(1)
        num_1 += 1
    else:
        num_1 = 0
        shutil.copytree("test_dir1", f"{url.url}/test_dir1")
        os.startfile(f"{url.url}/test_dir1/safe.py")