# template from nekitdev on github

from setuptools import setup
from pathlib import Path
import re

__version__ = "0.0.1"

root = Path(__file__).parent

requirements = (root / "requirements.txt").read_text("utf-8").splitlines()

version = __version__

long_description = (root / "README.md").read_text("utf-8")

setup(
    name="maple-cli",
    author="maple-ml",
    author_email="collinmcarroll@gmail.com",
    url="https://github.com/maple-ml/cli",
    project_urls={
        "Issue tracker": "https://github.com/maple-ml/cli/issues"
    },
    version=version,
    packages=["maple"],
    entry_points = {
        "maple": [
            "maple = maple.__main__:maple"
        ]
    },
    license="MIT",
    description="CLI utilities for maple",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.6",
)