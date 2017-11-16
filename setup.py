from setuptools import setup

setup(
    name='pynapple',
    version='0.1',
    description='A project which requires Python 3.6 to parse the setup file',
    url='https://github.com/wimglenn/pynapple',
    author='Wim Glenn',
    author_email='hey@wimglenn.com',
    license='MIT',
    packages=['pynapple'],
    # include_package_data=True,
    package_data={
        'pynapple': ['pynapple_package_data.dat'],
    },
    zip_safe=False,
    python_requires=f'>=3.6',
)
