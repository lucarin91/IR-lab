from processhtml import *

if __name__ == "__main__":
    data = html_to_data("pages/www.imdb.com/title/tt2554274/index.html")
    print data['title']
    print data['description']
