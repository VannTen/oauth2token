import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oauth2token",
    version="0.0.1",
    author="Max Gautier",
    author_email="ashelia1000@gmail.com",
    description="Oauth2 token management for cli applications",
    long_description=long_description,
    long_description_content_type="text/rst",
    url="https://github.com/VannTen/oauth2token",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL3",
        "Operating System :: OS Independent",
    ],
    scripts = [
        'bin/oauth2create',
        'bin/oauth2get'
    ],
    python_requires='>=3.6',
)
