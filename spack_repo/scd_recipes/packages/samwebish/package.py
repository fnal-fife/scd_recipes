# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Samwebish(Package):
    """Emulate SAM with metacat/declad/rucio"""

    homepage = "https://github.com/marcmengel/samwebish/"
    url = "https://github.com/fnal-fife/samwebish/archive/refs/tags/v2.0.1.tar.gz"
    git = "https://github.com/fnal-fife/samwebish.git"

    version("main", branch="main")
    version("develop", branch="main")
    version("0.1.alpha", sha256="63430864915d34cf2ad64a0fa557d32c059e5da8b8a46952570aa6b173fdaa29")
    version("0.4.alpha", sha256="f12611a51e9e51475c2343404e43d679a15fac8644793c75fab678b333a437fb")

    def url_for_version(self, version):
        url = "https://github.com/fnal-fife/samwebish/archive/refs/tags/{0}{1}.tar.gz"
        prefix = ""
        vstr = str(version)
        return url.format(prefix, vstr)

    depends_on("python")
    depends_on("py-fastapi",)
    depends_on("py-fastapi-utils",)
    depends_on("metacat")
    depends_on("data-dispatcher")
    depends_on("py-pyparsing")
    depends_on("py-rucio-clients")
    depends_on("py-typing-inspect")
    depends_on("py-python-multipart")
    depends_on("py-cryptography")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix)
        env.prepend_path("PATH", self.prefix)
