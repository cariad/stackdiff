from pathlib import Path

from setuptools import setup  # pyright: reportMissingTypeStubs=false

from changedifferently.version import get_version

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
    description="Visualises the changes described by an Amazon Web Services CloudFormation change set",
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="changedifferently",
    packages=[
        "changedifferently",
        "changedifferently.version",
    ],
    package_data={
        "changedifferently": ["py.typed"],
        "changedifferently.version": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/changedifferently",
    version=version,
)
