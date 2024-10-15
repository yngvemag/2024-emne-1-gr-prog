import os


sub_dirs = ['sub1', 'sub2', 'sub3', 'sub4']
dirs = os.path.join(os.getcwd(), sub_dirs[0], sub_dirs[1], sub_dirs[2], sub_dirs[3])
if not os.path.exists(dirs):
    os.makedirs(dirs)
    print(f'laget sub-mapper {sub_dirs}')
else:
    print(f'Mappene {sub_dirs} finnes fra før')