import sys
import os
import os.path
import pickle
import unicodedata
import warnings

from . import __meta__ as meta
from . import tools

try:
    import appdirs
    user_path = None
    if (
      # UNICODE_CATEGORIES_CACHE (enabled by default)
      (os.getenv('UNICODE_CATEGORIES_CACHE', '').lower() or '1')
      in ('1', 'yes', 'true' 'on', 'enable', 'enabled')
      ):
        user_path = '%s-cache.bin' % appdirs.user_cache_dir(
            meta.__app__,
            version='%s-%s' % (
                meta.__version__,
                unicodedata.unidata_version
                ))
except ImportError:
    user_path = None

if sys.version_info < (3, ):
    FileNotFoundError = IOError  # noqa
    PermissionError = IOError  # noqa

data_version = unicodedata.unidata_version.split('.')
module_version = meta.__version__.split('.')


def load_from_package():
    '''
    Try to load category ranges from module.

    :returns: category ranges dict or None
    :rtype: None or dict of RangeGroup
    '''
    try:
        import pkg_resources
        f = pkg_resources.resource_stream(
            meta.__app__,
            'cache/unicategories.cache'
            )
        dversion, mversion, data = pickle.load(f)
        if dversion == data_version and mversion == module_version:
            return data
        warnings.warn(
            'Unicode unicategories database is outdated. '
            'Please reinstall unicategories module to regenerate it.'
            if dversion < data_version else
            'Incompatible unicategories database. '
            'Please reinstall unicategories module to regenerate it.'
            )
    except (ValueError, EOFError):
        warnings.warn(
            'Incompatible unicategories database. '
            'Please reinstall unicategories module to regenerate it.'
            )
    except (ImportError, FileNotFoundError):
        pass


def load_from_cache(path=user_path):
    '''
    Try to load category ranges from userlevel cache file.

    :param path: path to userlevel cache file
    :type path: str
    :returns: category ranges dict or None
    :rtype: None or dict of RangeGroup
    '''
    if not path:
        return
    try:
        with open(path, 'rb') as f:
            dversion, mversion, data = pickle.load(f)
        if dversion == data_version and mversion == module_version:
            return data
    except (FileNotFoundError, ValueError, EOFError):
        pass


def generate_and_cache(path=user_path):
    '''
    Generate category ranges and save to userlevel cache file.

    :param path: path to userlevel cache file
    :type path: str
    :returns: category ranges dict
    :rtype: dict of RangeGroup
    '''
    data = tools.generate()
    if not path:
        return data
    try:
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(path, 'wb') as f:
            pickle.dump((data_version, module_version, data), f)
    except (PermissionError, ValueError) as e:
        warnings.warn('Unable to write cache file "%s": %s' % (path, e))
    return data
