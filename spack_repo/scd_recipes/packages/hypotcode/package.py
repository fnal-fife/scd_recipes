# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Hypotcode(Package):
    """Client package for SAM data management system webservice"""

    homepage = "https://fifewiki.fnal.gov/hypot"
    url = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/prod_mgmt_db-hypotcode.v2_0.tar"

    version("2.1", sha256="96261652218aa87366fcfa2182c3a209b49314889c860d517d602c849927bf5a")
    version("1.2", sha256="c92eb7f743070621e40681b2cfb35ebd9b09886625bb7e458da4011c3286c37a")
    version("1.1", sha256="0dd8d6e486b3f0d5ce5a9094d5ac708a59ab437e03abaa029b2f88764db4576e")

    def url_for_version(self, version):
        url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/prod_mgmt_db-hypotcode.v{0}.tbz2"
        return url.format(version.underscored)

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
