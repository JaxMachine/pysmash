from distutils.core import setup
import pysmash


setup(name="pysmash",
      author="Peter Wensel",
      url="https://github.com/PeterCat12/pysmash",
      description="python bindings for Smash.gg API",
      version=pysmash.__version__,
      packages=[
          'pysmash',
      ],
      install_requires=[
          'requests==2.10.0',
      ]
)
