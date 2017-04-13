import os
import os.path
from distutils import log
from distutils.core import Command


class create_content(Command):
    '''Distutils subcommand to generate package data'''

    description = 'Generate and install package data'

    user_options = []

    def initialize_options(self):
        self.install_dir = None
        self.package_content = None
        self.outfiles = []

    def finalize_options(self):
        self.set_undefined_options(
            'install',
            ('install_lib', 'install_dir'),
            )

        self.packages = self.distribution.packages
        self.package_content = self.distribution.package_content

    def run(self):
        log.info('Generating install files')
        for package, files in self.package_content.items():
            for path, fnc in files.items():
                base = os.path.dirname(path)
                if base and not os.path.exists(base):
                    os.makedirs(base)
                abspath = os.path.join(self.install_dir, package, path)
                fnc(abspath)
                self.outfiles.append(abspath)

    def get_inputs(self):
        return []

    def get_outputs(self):
        return self.outfiles
