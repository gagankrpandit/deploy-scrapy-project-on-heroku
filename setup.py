from setuptools import setup, find_packages

setup(
    name='flipkart_spider',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = flipkart_spider.settings']},
)
