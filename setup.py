from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="chat_exporter_hikari",
    version="2.5.1",
    author="h4ckd0tm3",
    author_email="marcel@schnideritsch.at",
    description="A simple Discord chat exporter for Python Discord bots.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h4ckd0tm3/DiscordChatExporterPy-hikari",
    packages=find_packages(),
    package_data={'': [r'chat_exporter/html/*.html']},
    include_package_data=True,
    license="GPL",
    install_requires=["aiohttp", "pytz", "grapheme", "emoji"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords="chat exporter",
)
