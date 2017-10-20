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
    scripts=[
        'shell_scripts/script1.sh',
        'shell_scripts/script2.sh',
    ],
    zip_safe=False,
    python_requires=f'>=3.6',
)
