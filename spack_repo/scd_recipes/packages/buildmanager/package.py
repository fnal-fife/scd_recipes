# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Buildmanager(Package):
    """multi platform build assistant"""

    homepage = "https://github.com/marcmengel/buildmanager"
    url = "https://github.com/marcmengel/buildmanager/archive/refs/tags/v1_12.tar.gz"

    maintainers("marcmengel")

    license("Apache")

    version("1.12", sha256="8344af340bd475f88920484bd07237beeb96a36362005d9dc1259635111dca80")

    depends_on("tk")
    depends_on("expect")

    def url_for_version(self, version):
        urlf = "https://github.com/marcmengel/buildmanager/archive/refs/tags/v{}.tar.gz"
        return urlf.format(version.underscored)

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, env):
        env.set("BUILDMANAGER_DIR", self.prefix)
        env.prepend_path("PATH", self.prefix.bin)
