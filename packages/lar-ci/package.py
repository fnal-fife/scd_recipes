# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class LarCi(Package):
    """Larsoft CI package"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/lar_ci/wiki"
    url = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/lar_ci.v3_7_0.tar"

    version("3.7.0", sha256="5d5071408f0a9ac9ad39d5392e25139af29528db8743578ef9dbdf2a4893d4b3")
    version("3.6.0", sha256="0adfdc4902088396b73263907e74c90809fd99c9daf09d5eb3efb9e041439e9e")

    def url_for_version(self, version):
        url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/lar_ci.v{0}.tbz2"
        return url.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/python")
