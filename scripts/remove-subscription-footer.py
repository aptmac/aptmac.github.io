import os
from bs4 import BeautifulSoup

# Solution inspired by: https://stackoverflow.com/a/48443581
directory = './static'
for root, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith('.html'):
            fname = os.path.join(root, filename)
            f = open(fname, "r")
            soup = BeautifulSoup(f, 'html.parser')
            element = soup.find("section", class_="footer-cta")
            if element:
                f.close()
                element.decompose()
                print('Removing footer from: ' + fname)
                f = open(fname, "w")
                f.write(str(soup))
            f.close()
