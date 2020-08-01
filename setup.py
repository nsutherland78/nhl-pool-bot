from setuptools import find_packages, setup

setup(name="nhl-pool-bot",
      description="NHL ",
      author="Nathan Sutherland",
      author_email="nathan.sutherland@gmail.com",
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'nhl-pool-bot = nhl-pool-bot:main',
          ],
      }
      )
