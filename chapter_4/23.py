import os
def my_find(path, file):
    if os.path.isfile(path):
        if path.split('/')[-1] == file:
            return [path]
        else:
            return []
    else:
        t = []
        for f in os.listdir(path):
            t+=my_find(os.path.join(path,f), file)
        return t

for x in my_find("../../../workdir/software/", "wine-qqintl.zip" ):
    print x
