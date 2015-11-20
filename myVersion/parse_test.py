import os
from processhtml import *

rootdir = "pages/www.imdb.com/title/"

if __name__ == "__main__":
    for subdir, dirs, files in os.walk(rootdir):
        for dir in dirs:
            move = os.path.join(subdir, dir, 'index.html')
            if os.path.isfile(move):
                str = html_to_data(move)
                str = str.split('(')
                print str[0]
