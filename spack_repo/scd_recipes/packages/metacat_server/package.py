# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *
import os


class MetacatServer(Package):
    """Client package for SAM data management system webservice"""

    homepage = "https://github.com/fermitools/metacat"
    url = "https://github.com/fermitools/metacat/archive/refs/tags/4.0.0.tar.gz"

    version("4.1.4", sha256="6de6562ed61820e0e41a57b0fb0bcb49d6103d02bbfeaaa32368ee74702cb6c4")
    version("4.1.3", sha256="058095e697a422241925367a22c386a6a6f31d0e33ebaa7e0aa27bbdd08b0f45")
    version("4.1.2", sha256="ff1c71c4f62ce689b6eea39af840e8e26f69de1fcf2f387dacf1e753e61d49d2") 
    version("4.0.2", sha256="be5151cc5265053061173cbe26dd20928b6a4d4fb7f9a4639436094a2d88ab62") 
    version("4.0.0", sha256="49836df3b7f2028c9b88c95a6904322373a9192d863e6756aec332bbe414fe85")


    def url_for_version(self, version):
        url = "https://github.com/fermitools/metacat/archive/refs/tags/{0}.tar.gz"
        return url.format(version.underscored)

    depends_on("python")
    depends_on("py-pyyaml")
    depends_on("py-kafka")
    depends_on("py-lark")
    depends_on("py-pyjwt")
    depends_on("py-pythreader")
    depends_on("py-requests")
    depends_on("py-stompymq")
    depends_on("py-webpie")
    depends_on("py-wsdbtools")
    depends_on("py-scitokens")
    depends_on("py-rucio-clients") # do we need this?

    def install(self, spec, prefix):
        with working_dir(self.stage.source_path):
            os.symlink("web_server", "server") 
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, run_env):
        run_env.prepend_path("PYTHONPATH", self.prefix)
