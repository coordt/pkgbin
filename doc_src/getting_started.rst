===============
Getting Started
===============

User accounts
   Creating
   Updating information
   

Managing packages
   Alter your .pypirc ::
   
      [distutils]
      index-servers =
          pypi
          pkgbin
      
      [pypirc]
      servers =
          pypi
          pkgbin
      
      [pkgbin]
      username:joecool
      password:Pa55w0rd
      repository:http://pkgbin.com/joecool/pypi/
      
      [pypi]
      username:joecool
      password:MyPa55w0rd
   
   Uploading packages
      python setup.py register -r pkgbin sdist upload -r pkgbin
   Browsing
      http://pkgbin.com/joecool/
   Giving access to packages
      Permissions
         Read only
         Read/write
      Users see them in their personal pypi



Organizations
   Creating
   Managing members
   Uploading packages
   Managing packages
      Browsing
      Public and private packages
