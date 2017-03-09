from setuptools import setup

setup(
    name='wft4galaxy',
    description='Utility module for testing Galaxy workflows',
    url='https://github.com/phnmnl/wft4galaxy',
    version='0.1',
    install_requires={
        'setuptools': ['setuptools'],
        'future': ['future>=0.16.0'],
        'bioblend': ['bioblend>=0.8.0'],
        'ruamel.yaml': ['ruamel.yaml'],  # TODO: to be removed in the next release
        'lxml': ['lxml'],
        'pyyaml': ['pyyaml'],
        'sphinx_rtd_theme': ['sphinx_rtd_theme'],
        'Jinja2': ['Jinja2>=2.9']
    },
    package_data={'templates': ['*']},
    packages=["wft4galaxy", "wft4galaxy.comparators", "templates"],
    scripts=['utils/docker/wft4galaxy-docker'],
    entry_points={'console_scripts': [
        'wft4galaxy = wft4galaxy.core:main',
        'wft4galaxy-wizard = wft4galaxy.wizard:main'
    ]}
)
