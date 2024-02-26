# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Declad(Package):
    """File Declaration Daemon for MetaCat/Rucio"""

    homepage = "https://github.com/fermitools/declad/"
    url = "https://github.com/fermitools/declad/archive/refs/tags/v2.0.1.tar.gz"

    version("2.0.3", sha256="1c7f2e6c340f593c6c39fc403066985f12d1fd5f79310a49caf00643f8b272f5")
    version("2.0.2", sha256="679faa6923fa3ea89eaa4af1bc92f88616e770e22ac5f87333d32936373eb324")
    version("2.0.1", sha256="8735e8ab894696d3e08614b1a09dc3dd9b97b62d2b1d14e90546f9ef80004376")


    def url_for_version(self, version):
        url = "https://github.com/fermitools/declad/archive/refs/tags/v{0}.tar.gz"
        return url.format(version.underscored)

    depends_on("py-webpie")
    depends_on("metacat")
    depends_on("sam-web-client")
    depends_on("rucio-clients")
    depends_on("py-jinja2")

    def install(self, spec, prefix):
        with working_dir("declad"):
            make("BUILD_DIR=%s" % prefix, "build")

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix)
        env.prepend_path("PATH", self.prefix)
        env.set("WEBPIE_SCRIPT_HOME", self.prefix)
