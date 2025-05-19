# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
import glob


class PyStompymq(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/imandr/stompymq"
    pypi = "stompymq/stompymq-1.1.1.tar.gz"

    version("1.1.1", sha256="8494d34c813beff6b366d5f9ca60e1d23b315bc88c47ed52bb42409fc039814f")

    license("UNKNOWN")

    depends_on("py-setuptools", type="build")

    def config_settings(self, spec, prefix):
        settings = {}
        return settings
