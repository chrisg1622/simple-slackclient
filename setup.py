import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='simple-slackclient',
    version='0.1',
    scripts=['simple-slackclient'],
    author="Chris George",
    author_email="chrisg1622@gmail.com",
    description="A simple slack API for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrisg1622/simple-slackclient",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ]
)
