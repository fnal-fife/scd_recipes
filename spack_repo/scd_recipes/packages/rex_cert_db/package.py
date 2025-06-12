# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class RexCertDb(Package):
    """Client package for REX certificate tracking database"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/rex-cert-db/wiki"
    url = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/rex-cert-db.v1_4.tar"

    version("1.4", sha256="40124d61c85563a96d96c999d26a2b149326f3e4543179b977fbea5fea6c44dc")

    def url_for_version(self, version):
        url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/rex-cert-db.v{0}.tbz2"
        return url.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/python")
