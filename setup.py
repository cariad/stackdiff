from pathlib import Path

from setuptools import setup  # pyright: reportMissingTypeStubs=false

from stackdiff.version import get_version

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Utilities",
    "Typing :: Typed",
]

version = get_version()

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Visualises the changes described by an Amazon Web Services CloudFormation stack change set",
    entry_points={
        "console_scripts": [
            "stackdiff=stackdiff.__main__:cli_entry",
        ],
    },
    include_package_data=True,
    install_requires=[
        "ansiscape   >= 1.1,   < 2.0",
        "boto3       >= 1.18,  < 2.0",
        "differently >= 1.0.1, < 2.0",
        "pyyaml      >= 6.0,   < 7.0",
        "tabulate    >= 0.8,   < 1.0",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="stackdiff",
    packages=[
        "stackdiff",
        "stackdiff.version",
    ],
    package_data={
        "stackdiff": ["py.typed"],
        "stackdiff.version": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/stackdiff",
    version=version,
)
