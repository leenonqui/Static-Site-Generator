import os
import shutil


def copy_to_dst(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    if not os.path.exists(src):
        raise Exception("Source path does not exists")
    if os.path.isfile(src):
        return
    for path in os.listdir(src):
        src_path = os.path.join(src, path)
        print()
        if os.path.isfile(src_path): # if path point to a file
            shutil.copy(src_path, dst) # copies file to destination
        else:
            dst_path = os.path.join(dst, path)
            copy_to_dst(src_path, dst_path)
