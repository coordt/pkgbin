=============
Organizations
=============

An organization is a non-loginable user placeholder for a group of users. Organizations allow for a central holding place for packages created and maintained by a team.

An organization has:

* A creator, who can do anything. This is a safety feature, in case they accidentally remove their permissions.

* Members. Members have several different permission levels:
   * *Admin.* They can adjust attributes of the organization, add/remove members, and everything that the other permissions allow.
   * *Create packages.* These members can register a new package for the organzation.
   * *Write packages.* These members can update existing packages, but not register new ones.
   * *Read packages.* These members can download packages only.

Creating an organization
========================

#. A user clicks on "Create Organization" from the left sidebar.

#. Set the organization's name.

#. Add members and set their permission level.

Using the organization
======================

Each member with package create or package write permission will have to modify their ``.pypirc`` files to include an entry for this organization::

   [distutils]
   index-servers =
       pypi
       pkgbin
       myorg

   [pypirc]
   servers =
       pypi
       pkgbin
       myorg

   [myorg]
   username:joecool
   password:Pa55w0rd
   repository:http://pkgbin.com/myorg/pypi/

   [pkgbin]
   username:joecool
   password:Pa55w0rd
   repository:http://pkgbin.com/joecool/pypi/

   [pypi]
   username:joecool
   password:MyPa55w0rd

In this example, an entry exists for ``myorg``. The username and password are the same as the entry for ``pkgbin``, but use the organization's URL.

Now when registering or uploading a package, specify ``-r myorg`` when registering or uploading.