
import sys

from setuptools.command.install import install as BaseInstall
from setuptools.dist import Distribution as BaseDistribution

from .cache import install_cache


class install(BaseInstall):
    sub_commands = BaseInstall.sub_commands + [
        ('install_cache', None),
        ]


class Distribution(BaseDistribution):
    default_cmdclass = {
        'install': install,
        'install_cache': install_cache,
        }

    package_content = None

    def __init__(self, attrs):
        cmdclass = self.default_cmdclass.copy()
        cmdclass.update(attrs.get('cmdclass', ()))
        attrs['cmdclass'] = cmdclass

        if sys.version_info < (3, ):
            BaseDistribution.__init__(self, attrs)
        else:
            super(Distribution, self).__init__(attrs)
