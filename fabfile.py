from fabric.api import *

def build():
    local('sphinx-build -b html -d _build/doctrees . _build/html')

def clean():
    local('rm -rf _build')


