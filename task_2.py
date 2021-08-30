import os
import shutil

new_dir = 'task3'
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

search = r'my_project'
files = []

for i, k, f, in os.walk(search):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(i, file))
for r in files:
    search = os.path.join(new_dir, os.path.basename(os.path.dirname(r)))
    if not os.path.exists(search):
        os.mkdir(search)
    save_path = os.path.join(search, os.path.basename(r))
    shutil.copy(r, save_path)