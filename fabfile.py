import requests
from fabric.api import local

def update():
    latest_version = requests.get('https://api.github.com/repos/driftyco/ionicons/releases/latest').json()['tag_name']
    local('wget https://github.com/driftyco/ionicons/archive/{0}.zip'.format(latest_version))
    local('unzip {0}.zip && rm {0}.zip'.format(latest_version))
    local('rm -rf css/*')
    local('rm -rf fonts/*')
    local('cp ionicons-{0}/css/ionicons.min.css css/'.format(latest_version[1:]))
    local('cp ionicons-{0}/fonts/* fonts/'.format(latest_version[1:]))
    local('rm -rf ionicons-{0}'.format(latest_version[1:]))
