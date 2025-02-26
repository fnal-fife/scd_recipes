# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyWebpie(PythonPackage):
    """WebPie (another way of spelling web-py) is a web application
    development framework for Python based on the WSGI standard."""

    homepage = "https://github.com/fermitools/webpie"
    pypi = "webpie/webpie-5.16.3.tar.gz"

    maintainers("marcmengel")

    license("BSD")

    version("5.16.3", sha256="7672844b3972dd98f5c0c5e256d84812daf841fcfd1ed7b0059e5928fffaffaf")

    depends_on("py-setuptools", type="build")
    depends_on("py-pythreader")

    def config_settings(self, spec, prefix):
        settings = {}
        return settings
