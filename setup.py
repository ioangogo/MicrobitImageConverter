from setuptools import setup

setup(name='mBitImageConverter',
      version='1.1',
      description='Converts any image format understood by PILLOW into a MicroBitImage',
      author='Ioan Loosley',
      author_email='legit.ioangogo@gmail.com',
      url='https://github.com/ioangogo/MicrobitImageConverter',
      packages=['mBitImageConverter'],
      install_requires=['pillow'],
      entry_points={'console_scripts': ['mBitImageConverter = mBitImageConverter.mBitImageConverter:main']}
     )
