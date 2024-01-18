# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Buildmanager(Package):
    """multi platform build assistant"""

    homepage = "https://github.com/marcmengel/buildmanager"
    url = "https://github.com/marcmengel/buildmanager/archive/refs/tags/v1_12.tar.gz"

    maintainers("marcmengel")

    license("Apache")

    version("1_12", sha256="575852e0c35e343b73ed1940da25976380d340966df48f2f2bb7e91a286a525d")

    depends_on("tk")
    depends_on("expect")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, env):
        env.set("BUILDMANAGER_DIR", self.prefix)
        env.prepend_path("PATH", self.prefix.bin)
