# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFiletransferservice(PythonPackage):
    """Fermi File Transfer Service -- transfer and declare files placed in a dropbox"""

    homepage = "http://cdcvs.fnal.gov/redmine/projects/filetransferservice"
    url = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/filetransferservice.v6_3_5.tar"

    version(
        "6.3.5",
        sha256="3ca8b2507d56b2a836cd8141c200a4618f9e22fd54d5478e69208bbfd0d21643",
    )

    depends_on("python@2.7.0:2.7.99", type=("build","run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-twisted", type=("build", "run"))
    depends_on("py-service-identity", type=("build", "run"))
    depends_on("py-pyopenssl", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-crcmod", type=("build", "run"))
    depends_on("py-sam-cp", type="run")
    depends_on("ifdhc cxxstd=11", type="run")

    @run_before('install')
    def set_version(self):
        import os
        with open("python/fts/_version.py","w") as of:
            of.write('version="{0}"'.format(self.spec.version))
        try:
            os.rmdir("sam-cp")
        except:
            pass
        os.symlink(self.spec["py-sam-cp"].prefix, "sam-cp")

#    @property
#    def build_directory(self):
#        """The root directory of the Python package.
#
#        This is usually the directory containing one of the following files:
#
#        * ``pyproject.toml``
#        * ``setup.cfg``
#        * ``setup.py``
#        """
#        return self.pkg.stage.source_path
#
