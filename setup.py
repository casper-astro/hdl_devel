from setuptools import setup, find_packages


setup(
    name = 'casper',
    version = '0.1',
    packages = find_packages(),

    install_requires = ['myhdl>=0.7'],

    package_data = {
        '': ['*.v', '*.vpi'],
    },

    test_suite = 'nose.collector',
    tests_require = 'nose',

)
