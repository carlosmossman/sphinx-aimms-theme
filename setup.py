from distutils.core import setup
import setuptools
import sys


setup(
    
    name = "sphinx_aimms_theme",
    version = '0.0.1',
    license = "MIT",
    packages= ['sphinx_aimms_theme'],
    url = "https://gitlab.com/ArthurdHerbemont/sphinx-aimms-theme",
    description = 'AIMMS theme for Sphinx',
    long_description=open('README.md').read(),
    author = "AIMMS User Support",
    author_email = "support@aimms.com",

    
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_aimms_theme = sphinx_aimms_theme',
        ]        
    },
    install_requires=[
       'sphinx',
       'sphinx_rtd_theme',
    ],
    package_data={'sphinx_aimms_theme': [
        'theme.conf',
        '*.html',
        'static/*.css',
        'static/*.js',
        'static/*.png',
        'static/icons/*.*'
    ]},
    include_package_data=True,

)