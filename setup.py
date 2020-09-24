import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="castervoice",
    author="To be determined",
    author_email="to@be.determined",
    description="Please describe me",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dictation-toolbox/Caster",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3"
            "or later (LGPLv3+)"
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "PyYAML",
        "dragonfly2"
    ]
)
