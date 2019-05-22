from function import *
from config import *
import subprocess
import os


if __name__ == '__main__':

    os.chdir(directory)
    # 获取各个part标题，及 视频总标题
    _, prefix = get_index(url.format(av, 1))
    # 重命名文件，去掉公共前缀，可单独运行rename_file，以重命名所有文件
    # prefix = '【Python-Django】2018年最新的Python3yuDjango打造爱家租房项目实战'
    rename_file(prefix=prefix)

    while start <= end:
        try:
            # print(start, end='\t')
            cmd = 'you-get -o {directory} {}'.format(url.format(av, start), directory=directory)
            result = subprocess.call(cmd, timeout=timeout)
            if result == 0:
                print('Download Success!--> Rename...', end='')
                rename_file(path=directory, num=start)
                print('OK')
            else:
                print('Download Fail!')
            start += 1
        except subprocess.TimeoutExpired:
            continue
        except AttributeError as e:
            print(e)
            start += 1
            continue
        except Exception as e:
            break