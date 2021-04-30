"""
This is where the implementation of the plugin code goes.
The MiniProjectCodeGenerator-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
import json
import os
import random
import shutil
from mako.template import Template
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('MiniProjectCodeGenerator')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class MiniProjectCodeGenerator(PluginBase):
    def main(self):
        core = self.core
        META = self.META
        root_node = self.root_node
        active_node = self.active_node

        name = core.get_attribute(active_node, 'name')

        logger.info('ActiveNode at "{0}" has name {1}'.format(core.get_path(active_node), name))

        core.set_attribute(active_node, 'name', 'newName')
        commit_info = self.util.save(root_node, self.commit_hash, self.branch_name, 'Python plugin updated the model')
        
      