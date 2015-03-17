import requests
from fabric.api import local

def update():
    latest_version = requests.get('https://api.github.com/repos/driftyco/ionicons/releases/latest').json()['tag_name']
    # local('rm -rf fonts/')
    # local('rm -rf css/')
    local('wget https://github.com/driftyco/ionicons/archive/{0}.zip'.format(latest_version))
    local('unzip {0}.zip'.format(latest_version))
    local('rm {0}.zip'.format(latest_version))
    # local('rm katex/README.md')
    # local('mv katex/* .')
    local('rm -rf ionicons-{0}'.format(latest_version[1:]))
