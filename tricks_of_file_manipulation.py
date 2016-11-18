# Fangyu
# 11/7/2016
# tricks of moving, copying, renaming files, etc.


# list all files
os.listdir(src)
# rename
os.rename(src, dst)
# copy

shutil.copyfile(src, dst, follow_symlinks=True)
