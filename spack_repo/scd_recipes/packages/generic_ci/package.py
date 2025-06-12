# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class GenericCi(Package):
    """Base CI package"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/ci/wiki"
    url = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/ci-generic.v2_0_0.tar"

    version("2.0.0", sha256="b427d34fbff761f39f6307e9e4185d22550dd8f8916397fc3dcaf31342d764a9")

    def url_for_version(self, version):
        url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/ci-generic.v{0}.tbz2"
        return url.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/python")
