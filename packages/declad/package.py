# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Declad(Package):
    """File Declaration Daemon for MetaCat/Rucio"""

    homepage = "https://github.com/marcmengel/declad/"
    url = "https://github.com/marcmengel/declad/archive/refs/tags/v2.0.1.tar.gz"

    version("2.0.1", sha256="8735e8ab894696d3e08614b1a09dc3dd9b97b62d2b1d14e90546f9ef80004376")
    version("2.0.2", sha256="78784dfa512e1381e8d089e3e7b20a4a333ddaac7606b402cf50f25ef4affacb")


    def url_for_version(self, version):
        url = "https://github.com/marcmengel/declad/archive/refs/tags/v{0}.tar.gz"
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
