import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oauth2token",
    version="0.0.2-1",
    author="VannTen",
    author_email="ashelia1000@gmail.com",
    description="Oauth2 token management for cli applications",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/VannTen/oauth2token",
    packages=setuptools.find_packages(where='.'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: End Users/Desktop",
        "Development Status :: 2 - Pre-Alpha"
    ],
    scripts = [
        'bin/oauth2create',
        'bin/oauth2get'
    ],
    python_requires='>=3.6',
    install_requires=[
        'google_auth_oauthlib',
        'pyxdg'
    ]
)
