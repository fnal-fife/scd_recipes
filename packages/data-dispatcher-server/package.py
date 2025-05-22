# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class DataDispatcherServer(Package):
    """Client package for SAM data management system webservice"""

    homepage = "https://github.com/fermitools/data_dispatcher"
    url = "https://github.com/fermitools/data_dispatcher/archive/refs/tags/1.26.4.tar.gz"
    git = "https://github.com/fermitools/data_dispatcher.git"

    version("2.0.2", sha256="ed517a202b0860562623d45cfa4d83141bf0ad36fd4220cdaf54f1d5878d5f1f") # FIXME
    version("2.0.1", sha256="176605877772f72af4b2b9e8442b9285e0d56dc2693f1a71aa1fb8ab44bad63c") # FIXME
    version("1.26.4", sha256="1bd1b5433a7e3d9b29917510531225abee17e8690d87d9eb0ccff2ad58cd72c9")
    version("1.26.2", sha256="0eaf99e65b5d5664a6524f81d31f387324bbe881570a0421532f24cefb7169c2")
    version("1.26.0", sha256="2d56d4c688bcd44c72887fa009875935402890d69c872399fe3112e4096483f7")
    version("main", branch="main")

    def url_for_version(self, version):
        url = "https://github.com/fermitools/data_dispatcher/archive/refs/tags/{0}.tar.gz"
        return url.format(version.underscored)

    depends_on("python")
    depends_on("py-kafka")
    depends_on("py-lark")
    depends_on("py-pyjwt")
    depends_on("py-pythreader")
    depends_on("py-requests")
    depends_on("py-stompymq")
    depends_on("py-webpie")
    depends_on("py-wsdbtools")
    depends_on("metacat")
    depends_on("rucio-clients")

    def install(self, spec, prefix):
        with working_dir(self.stage.source_path):
            os.symlink("web_server", "server")
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, run_env):
        run_env.prepend_path("PYTHONPATH", self.prefix)
