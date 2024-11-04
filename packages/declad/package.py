# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Declad(Package):
    """File Declaration Daemon for MetaCat/Rucio"""

    homepage = "https://github.com/fermitools/declad/"
    url = "https://github.com/fermitools/declad/archive/refs/tags/v2.0.1.tar.gz"

    version("2.3.0", sha256="eb0c4aaec0fdf653cbbf26f3ee8a39bf4e2bfaf65aad185157e8f55bdbfc0649") 
    version("2.2.0", sha256="9db73c2b537c7d236fb32b94db6aec9e383434acfa9e6101f7569375ed738f0f") 
    version("2.1.0.pre", sha256="9704542ea228d0b81c6323356d6a9685ee13261937b2d4006b0e77c3b16a10ed")
    version("2.0.4", sha256="e08d724d32697139b83f5aab8eecd4cf9191f131ada0e21fae50748f06909059")
    version("2.0.3", sha256="1c7f2e6c340f593c6c39fc403066985f12d1fd5f79310a49caf00643f8b272f5")
    version("2.0.2", sha256="679faa6923fa3ea89eaa4af1bc92f88616e770e22ac5f87333d32936373eb324")
    version("2.0.1", sha256="8735e8ab894696d3e08614b1a09dc3dd9b97b62d2b1d14e90546f9ef80004376")


    def url_for_version(self, version):
        url = "https://github.com/fermitools/declad/archive/refs/tags/{0}{1}.tar.gz"
        if version < Version("2.2.0"):
            prefix = version
            vstr=version.underscored
        else:
            prefix = ""
            vstr=str(version)
        return url.format(prefix, vstr)

    depends_on("py-webpie")
    depends_on("metacat")
    depends_on("sam-web-client")
    depends_on("rucio-clients")
    depends_on("py-jinja2")
    depends_on("py-fadvise")

    def install(self, spec, prefix):
        with working_dir("declad"):
            make("BUILD_DIR=%s" % prefix, "build")

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix)
        env.prepend_path("PATH", self.prefix)
        env.set("WEBPIE_SCRIPT_HOME", self.prefix)
