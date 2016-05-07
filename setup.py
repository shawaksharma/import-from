from setuptools import setup

setup(name='importfromtwitter',
      version='1.0.1',
      description='Host and import your python functions from Twitter!',
      long_description='Disclaimer: This is not a serious project, just a bit of fun.',
      url='https://github.com/libeclipse/import-from-twitter',
      author='libeclipse',
      author_email='libeclipse@gmail.com',
      license='MIT',
      packages=['importfromtwitter'],
      install_requires=["beautifulsoup4", "requests"],
      keywords = ['importfromtwitter', 'import', 'from', 'twitter', 'host'],
      zip_safe=False)
