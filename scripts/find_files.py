"""
find docker-compose.yml files
"""

import fnmatch
import os
from shutil import copyfile
from natsort import natsorted


def find_yml_files(path):
    """
    find docker-compose.yml files in path
    """
    matches = {}
    for root, _, filenames in os.walk(path, followlinks=True):
        for _ in set().union(fnmatch.filter(filenames, 'docker-compose.yml'), fnmatch.filter(filenames, 'docker-compose.yaml')):
            key = root.split('/')[-1]
            matches[key] = os.path.join(os.getcwd(), root)
    return matches


def get_readme_file(path):
    """
    find case insensitive readme.md in path and return the contents
    """

    readme = None

    for file in os.listdir(path):
        if file.lower() == "readme.md" and os.path.isfile(os.path.join(path, file)):
            file = open(os.path.join(path, file))
            readme = file.read()
            file.close()
            break

    return readme


def get_logo_file(path):
    """
    find case insensitive logo.png in path and return the contents
    """

    logo = None

    for file in os.listdir(path):
        if file.lower() == "logo.png" and os.path.isfile(os.path.join(path, file)):
            file = open(os.path.join(path, file))
            logo = file.read()
            file.close()
            break

    return logo


def get_versions(path):
    """
    find versions available under the 'versions' folder.
    """
    
    matches = []
    
    if os.path.isdir(os.path.join(path, 'versions')):
      for root, _, filenames in os.walk(os.path.join(path, 'versions')):
        for name in _:
          matches.append(name)
    return { 'data' : natsorted(matches, reverse=True) }
  

def change_version(path, version):
    """
    change version for a project
    """
    
    if os.path.isdir(os.path.join(path, 'versions')):
      for root, _, filenames in os.walk(os.path.join(path, 'versions')):
        for name in _:
          if name == version:
            copyfile(os.path.join(path, 'versions', version, 'docker-compose.template.yml'), os.path.join(path, 'docker-compose.yml'))
    return "ok"
