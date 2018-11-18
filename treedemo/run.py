from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import urllib.request

from collections import namedtuple

from bs4 import BeautifulSoup
from absl import flags
from absl import app

import pdb

Node = namedtuple("Node", ["id", "name", "parent", "children"])

class Tree(object):
    """ Tree """
    
    def __init__(self):
        self.nodes = []

    def add_node(self):
        pass
        
    def search(self, id="", name=""):
        pass


def parse_line(line):
    code = int(line[5:11])
    level = 0
    name = ""
    for item in line[11:-1]:
        if item == '\u3000':
            level += 1
        else:
            name = name + item
    return code, name, level


def build_tree_from_url(url):
    tree = Tree()
    response = urllib.request.urlopen(website)
    html_doc = response.read().decode("utf-8")
    soup = BeautifulSoup(html_doc, 'html.parser')
    first = True
    node = Node()
    children = []
    for line in soup.areacode:
        code, name, level = parse_line(line)
        
    
def main(unused_argv):
    del unused_argv
    url = "http://www.zxinc.org/gb2260-latest.htm"
    build_tree_from_url(url)
    pdb.set_trace()
    
if __name__ == "__main__":
    app.run(main)

