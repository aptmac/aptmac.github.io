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
            elements = soup.findAll("a", class_="gh-head-button")
            for element in elements:
                if element:
                    f.close()
                    element['href'] = 'https://github.com/aptmac'
                    element['title'] = 'GitHub'
                    element['target'] = '_blank'
                    element.string = 'GitHub'
                    print('Adjusting header button in: ' + fname)
                    f = open(fname, "w")
                    f.write(str(soup))
                f.close()
