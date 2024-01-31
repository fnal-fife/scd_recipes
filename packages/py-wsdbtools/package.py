# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyWsdbtools(Package):
    """Client package for SAM data management system webservice"""

    homepage = "https://github.com/fermitools/data_dispatcher"
    url = "https://github.com/fermitools/wsdbtools/archive/refs/tags/1.9.3.tar.gz"
    version("1.9.3", sha256="362595edaabc647d94bd74c8073d7e52a02e3afe3162524b8d89777a874d3c4b")

    def url_for_version(self, version):
        url = "https://github.com/fermitools/wsdbtools/archive/refs/tags/{0}.tar.gz"
        return url.format(version.underscored)

    depends_on("python")
    depends_on("py-psycopg2")
    depends_on("py-webpie")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, run_env):
        run_env.prepend_path("PYTHONPATH", self.prefix)
