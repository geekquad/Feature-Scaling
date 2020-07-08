from distutils.core import setup
setup(
  name = 'Feature Scaling',         # How you named your package folder (MyLib)
  packages = ['featurescaler'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package that can transform features by scaling each feature into a given range.',   # Give a short description about your library
  author = 'GEEKQUAD',                   # Type in your name
  author_email = 'adityaastranaut@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/geekquad',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/geekquad/Feature-Scaling', 
  keywords = ['Feature_Scaling', 'Feature_Rescaling'],   # Keywords that define your package best
  install_requires=['numpy'],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)