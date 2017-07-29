import os
from setuptools import find_packages, setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-mpdcontroller",
    version = "0.1.2",
    packages=find_packages(),
    author = "Nicolas Wavrant",
    author_email = "nicolas.wavrant@gmail.com",
    description = ("A web interface to command the music player daemon service (mpd)."),
    license = "BSD",
    keywords = "django interface mpd client",
    url = "https://github.com/Sebatyne/django-mpdcontroller",
    #long_description = read('README.md'),
    classifiers = [
        "Environment :: Web Environment",
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
