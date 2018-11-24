from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import urllib.request

from collections import namedtuple

from bs4 import BeautifulSoup
from absl import flags
from absl import app

import pdb

Node = namedtuple("Node", ["id", "name", "parent_id", "children_ids", "level"])

class Tree(object):
    """ Tree """
    
    def __init__(self):
        self.nodes = {}
        self.nodes["root"] = Node("root", "root", "", [], -1)

    def add_node(self, node):
        self.nodes.append(node)
        
    def search(self, id="", name=""):
        pass

    def parse_line(self, line):
        code = int(line[:6])
        level = 0
        name = ""
        for item in line[6:]:
            if item == '\u3000':
                level += 1
            else:
                name = name + item
        return code, name, level

    def get_node(self, id):
        return self.nodes[id]

    def get_node_level(self, id):
        return self.nodes[id].level

    def get_parent_id(self, id):
        return self.nodes[id].parent_id
    
    def build_tree_from_url(self, url):
        response = urllib.request.urlopen(url)
        html_doc = response.read().decode("utf-8")
        soup = BeautifulSoup(html_doc, 'html.parser')
        last_node_id = "root"
        for line in soup.areacode:
            if len(line) <= 5:
                continue
            line = line.strip()
            code, name, level = self.parse_line(line)
            while (level < self.get_node_level(last_node_id)):
                last_node_id = self.get_parent_id(last_node_id)
            if (level == self.get_node_level(last_node_id)):
                parent_id = last_node_id
            elif level == self.get_node_level(last_node_id) + 1:
                parent_id = last_node_id
            else:
                pdb.set_trace()
                raise ValueError()
            node = Node(id=code, name=name, parent_id=parent_id, children_ids=[], level=level)
            self.nodes[code] = node
            self.nodes[parent_id].children_ids.append(code)
            last_node_id = code
            
    
def main(unused_argv):
    del unused_argv
    url = "http://www.zxinc.org/gb2260-latest.htm"
    tree = Tree()
    tree.build_tree_from_url(url)
#    pdb.set_trace()
    
if __name__ == "__main__":
    app.run(main)

