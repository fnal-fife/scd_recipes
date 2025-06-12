# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


def ignore_CVS(path):
    if str(path).find("CVS") >= 0:
        return True
    return False


class Telephone(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.www-tele.fnal.gov"
    cvs = ":pserver:anonymous@cdcvs.fnal.gov:/cvs/cd_read_only%module=telephone"
    maintainers = ["marcmengel"]

    version("v5_4")
    version("v5_3")
    version("v5_2")

    depends_on("perl-libwww-perl")
    # using ansi2html instead of old man2html...
    depends_on("py-ansi2html", type="build")
    # ansi2html uses code from setuptools?!..
    depends_on("py-setuptools", type="build")

    def patch(self):
        filter_file(
            "man2html",
            "ansi2html",
            "html/Makefile",
        )

    def install(self, spec, prefix):
        make = which("make")
        make()
        install_tree(self.stage.source_path, prefix, ignore=ignore_CVS)
