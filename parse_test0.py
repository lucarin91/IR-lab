import os
from processhtml import *

rootdir = "pages/www.imdb.com/title/"

if __name__ == "__main__":
    for subdir, dirs, files in os.walk(rootdir):
        for dir in dirs:
            move = os.path.join(subdir, dir, 'index.html')
            if os.path.isfile(move):
                data = html_to_data(move)
                print "\n"
                print data['title']
                print data['date']
                print data['description']
                print "\n"
