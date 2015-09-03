from setuptools import setup

#In Progress

setup(
    name='DashServ',
    version='0.1.0',
    author='Travis Noles',
    author_email = 'travis@noles.pw',
    description = '',
    license='GNU-afredo',
    url='',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hello=hello:cli
    '''
)