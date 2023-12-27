from setuptools import setup, find_packages

setup(
    name="binary-gutenberg",
    version="0.1.0",
    url="https://github.com/cjbackman/binary-gutenberg.git",
    author="Carl-Johan Backman",
    author_email="carljohan.backman@gmail.com",
    description="A tool to make scanned PDFs editable.",
    packages=find_packages(),
    install_requires=[
        "click >= 8.1.3",
        "openai >= 1.6.1",
    ],
    extras_require={
        "dev": [
            "jupyterlab",
        ]
    },
    entry_points={
        "console_scripts": [
            "bg=bin.cli:cli",
        ],
    },
)
