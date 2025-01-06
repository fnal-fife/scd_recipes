# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class JobsubLite(Package):
    """HTCondor Job submission wrappers from Fermilab"""

    homepage = "https://github.com/marcmengel/jobsub_lite"
    url = "https://github.com/marcmengel/jobsub_lite/archive/refs/tags/beta12.tar.gz"

    version("0.1.1",  sha256="8e989495c389a467d967a9cfcfbd26725f805ef23720cac22230abed1f385fad")
    version("0.1",    sha256="e4653eb5f9907251471fb5320e640e68b85f0c207ae3ec686c0f26aaf69ac21f")
    version("beta13", sha256="9cabd66158066d1288d7658ca5bf13d6480aaaa9f933ced63052c8cb38d8d403")
    version("beta12", sha256="fbdd54966216c3d017f65f255b0f4dc07efe69a0ead1086a375f7e625f3f3cc1")
    version("beta11", sha256="76e67503377103ca8b5a5aff7ad4189ebe02ae8e3f8ac5e5bc19bee9d124f428")
    version("beta10", sha256="b9cfc4dd93bfb5308ae411982cec26d83480867d9a3ac15dd46c00d1688b8cf0")
    version("beta9",  sha256="ea7ed67c410283b421f5ec54c76cab86eee2f920f7191530eb8142d545bd8505")

    def url_for_version(self, version):
        url = "https://github.com/marcmengel/jobsub_lite/archive/refs/tags/{0}.tar.gz"
        return url.format(version)

    variant("fullstack", default=False)

    depends_on("python@3.6.8:", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("htcondor@9.0.6:", type="run", when="+fullstack")
    depends_on("cigetcert", type="run")
    depends_on("htgettoken", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
