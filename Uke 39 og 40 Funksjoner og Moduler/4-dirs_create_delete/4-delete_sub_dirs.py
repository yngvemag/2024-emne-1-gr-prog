import os
import shutil # shell utility


sub_dirs = ['sub1', 'sub2', 'sub3', 'sub4']
dirs = os.path.join(os.getcwd(), sub_dirs[0])

if os.path.exists(dirs):
    shutil.rmtree(dirs)
    print(f'Slettet mappene {sub_dirs}')
else:
    print(f'Mappene {sub_dirs} finnes ikke')