# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ArtFhiclMode(Package):
    """Emacs mode for Art Fhicl files"""

    homepage = "https://github.com/knoepfel/art-fhicl"
    url = "https://github.com/knoepfel/art-fhicl/archive/refs/tags/0.4.tar.gz"

    version("0.4", sha256="1445d9ec14f75015b7861f5f38051d7e15f4d061e2eaeb6e70a0f672da5defea")

    def url_for_version(self, version):
        url = "https://github.com/knoepfel/art-fhicl/archive/refs/tags/{0}.tar.gz"
        return url.format(version)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/python")
