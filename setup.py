
from setuptools import setup
import empiriciSN

setup(
    name="empiriciSN",
    version='0.0.1',
    author="Tom Holoien",
    author_email="tholoien@gmail.com",
    url="https://github.com/tholoien/empiriciSN",
    packages=["empiriciSN"],
    description="Generate realistic parameters for a SN given host galaxy observations based on empirical correlations from SN datasets.",
    long_description=open("README.md").read(),
    package_data={"": ["README.md", "LICENSE"]},
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    install_requires=["numpy", "xdgmm", "scipy"],
)
