from setuptools import setup, find_packages

setup(
    name="pypack",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List other dependencies here
    ],
    description="A collection of tools to simplify your Python experience!",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Ollie Quayle",
    author_email="your.email@example.com",
    license="MIT",
    url="https://github.com/Ollieq1977336/PyPack",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
