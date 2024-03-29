"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

def plugin_files(name):
    return [
        'plugins/{0}/info.yaml'.format(name),
        'plugins/{0}/{0}.py'.format(name),
        'plugins/{0}/{0}.md'.format(name),
        'plugins/{0}/{0}.png'.format(name),
        'plugins/{0}/{0}_large.png'.format(name),
    ]

setup(
    name='psynteract-os',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.9.0',

    description='Psynteract OpenSesame Integration',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/psynteract/psynteract-os',

    # Author details
    author='Felix Henninger & Pascal Kieslich',
    author_email='mailbox@felixhenninger.com',

    # Choose your license
    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='psychology economics experiment strategy interaction',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'psynteract @ https://github.com/psynteract/psynteract-py/releases/download/v0.9.0/psynteract-0.9.0.tar.gz#egg=psynteract-0.9.0'
    ],

    #dependency_links = [
        
    #],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #entry_points={
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
    #},

    data_files = [
        ('share/opensesame_extensions/psynteract_extension', [
            'extensions/psynteract_extension/info.yaml',
            'extensions/psynteract_extension/psynteract_extension.py',
        ]),
        ('share/opensesame_plugins/psynteract_communicate',
         plugin_files('psynteract_communicate')),
        ('share/opensesame_plugins/psynteract_connect',
         plugin_files('psynteract_connect')),
        ('share/opensesame_plugins/psynteract_get',
         plugin_files('psynteract_get')),
        ('share/opensesame_plugins/psynteract_push',
         plugin_files('psynteract_push')),
        ('share/opensesame_plugins/psynteract_reassign',
         plugin_files('psynteract_reassign')),
        ('share/opensesame_plugins/psynteract_wait',
         plugin_files('psynteract_wait')),
    ]
)
