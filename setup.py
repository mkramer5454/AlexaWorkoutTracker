from setuptools import setup, find_packages

setup(
  name="Alexa",
  version="0.1",
  author="Matt Kramer",
  packages=find_packages(),
  install_requires=[
    'ask-sdk',
    'boto3',
    'botocore'
  ]
)
