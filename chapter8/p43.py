#usr/bin/env python

import sys
import os


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def validation_check(site_name, author, javascript, css):
    if len(site_name.strip()) == 0:
        print("Please enter correct site_name!")
        sys.exit()
        
    if len(author.strip()) == 0:
        print("Please enter correct author!")
        sys.exit()
    
    if javascript.upper() != 'N' and javascript.upper() != 'Y':
        print("javaScript answer just input \'y\' or \'n\'.")
        sys.exit()

    if css.upper() != 'N' and css.upper() != 'Y':
        print("CSS answer just input \'y\' or \'n\'.")
        sys.exit()


def make_directory(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        print("Created ./%s" % path)        


def make_index_file(base_path, site_name, author):
    path = "%s/index.html" % base_path
    with open(path, 'w') as f:
        f.write("<html>\n<head>\n")
        f.write("<title>%s</title>\n" % site_name)
        f.write("<meta name=\"%s\" content=\"%s\" />\n" % ("author", author))
        f.write("</head>\n</html>\n")
    print("Created ./%s" % path)


def create_site(site_name, author, javascript, css):
    base_path = site_name.strip().replace(" ","_")
    make_directory(base_path)
    make_index_file(base_path, site_name, author)    

    if javascript.upper() == 'Y':
        path = "%s/%s" % (base_path, "js")
        make_directory(path)

    if css.upper() == "Y":
        path = "%s/%s" % (base_path, "css")
        make_directory(path)
        
    

if __name__ == "__main__":
    site_name = version_input("Site name: ")
    author = version_input("Author: ")
    javascript = version_input("Do you want a folder for JavaScript?(y/n) ")
    css = version_input("Do you want a folder for CSS?i(y/n) ")

    validation_check(site_name, author, javascript, css)
    create_site(site_name, author, javascript, css)

