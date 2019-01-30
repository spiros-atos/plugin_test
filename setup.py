from setuptools import setup

setup(
    name='spiros',
    description='Test python script integration into cloudify plugin',
    packages=['plugin_master'],
    install_requires=[
      "cloudify-plugins-common"
      ]
    )
