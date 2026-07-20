from setuptools import setup

setup(
    name="kudocli",
    version="0.1.0",
    py_modules=["main", "client", "analyzer", "config_env_example", "get_token_example"],
    install_requires=[
        "rich>=13.0.0",
        "stravalib>=0.10.4",
        "python-dotenv>=1.0.0",
        "requests>=2.28.0"
    ],
    entry_points={
        "console_scripts": [
            "kudo=main:main"
        ]
    },
    author="Sarah Lima",
    description="KudoCli: Análise OSINT de atletas Strava",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
)
