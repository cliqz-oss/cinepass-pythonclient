from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    author='Konstiantyn Snihyr',
    author_email='konstantin.s@cliqz.com',
    name='cinepass-pythonclient',
    version='0.2',
    provides=['cinepass'],
    url='https://github.com/cliqz/cinepass-pythonclient',
    license='MIT',
    packages=[
        'cinepass',
        'cinepass.client',
        'cinepass.client.v4',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
    platforms='any',
    tests_require=[
        'pytest',
    ]
)
