import os

from django.core.files.storage import FileSystemStorage
from django.conf import settings

from cumulus.storage import CloudFilesStorage

from queued_storage.backends import QueuedFileSystemStorage

DEFAULT_ROOT = os.path.join(settings.MEDIA_ROOT_PREFIX, 'assets')
DEFAULT_URL = '%smedia/' % settings.MEDIA_URL_PREFIX

class MediaStorage(FileSystemStorage):
    def __init__(self, location='', base_url='', *args, **kwargs):
        real_location = os.path.join(DEFAULT_ROOT, location)
        real_base_url = "%s%s" % (DEFAULT_URL, base_url)
        super(MediaStorage, self).__init__(real_location, real_base_url, *args, **kwargs)

class QueuedUserCloudFilesStorage(QueuedFileSystemStorage):
    def __init__(self, remote='cumulus.storage.CloudFilesStorage', *args, **kwargs):
        super(QueuedGridFSStorage, self).__init__(remote=remote, *args, **kwargs)

class UserCloudFilesStorage(CloudFilesStorage):
    """
    User the callable for the upload_to to prefix the username to the file for
    storage.
    
    In save, use that prefix to load a container instead of a directory.
    """
    def _save(self, name, content):
        (path, last) = os.path.split(name)
        self.container = self.connection.get_container(path)
        super(UserCloudFilesStorage, self)._save(last, content)