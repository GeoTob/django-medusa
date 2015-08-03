from setuptools import setup, find_packages

install_requires = [
    'django',
]

version = "0.3.1"

setup(name='django-medusa-unstoppable',
    version=version,
    description='A Django static website generator. Fork of django-medusa',
    author='Tobias Schulmann', # update this as needed
    author_email='tobiasschulmann@catalyst.net.nz', # update this as needed
    url='https://github.com/GeoTob/django-medusa-unstoppable',
    download_url='https://github.com/GeoTob/django-medusa-unstoppable/releases/tag/0.3.1',
    packages=find_packages(),
    install_requires=install_requires,
    license='MIT',
    keywords='django static staticwebsite staticgenerator publishing',
    classifiers=["Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
