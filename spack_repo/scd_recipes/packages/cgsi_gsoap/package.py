# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install cgsi-gsoap
#
# You can edit this file again by typing:
#
#     spack edit cgsi-gsoap
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class CgsiGsoap(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "http://dmc.web.cern.ch/"
    url = "https://gitlab.cern.ch/dmc/cgsi-gsoap/-/archive/v1.3.11/cgsi-gsoap-v1.3.11.tar.gz"

    maintainers = [
        "marc.mengel@gmail.com",
    ]

    version(
        "1.3.11",
        sha256="5fe3d8741f906dc77a13e61871d18bcf0a6deab6dd70fb0b0c977b4ef61ff924",
    )
    version(
        "1.3.10",
        sha256="17222279fe26697bb45f168039e21c4324015545d6741038792cd9df746647f8",
    )
    version(
        "1.3.9",
        sha256="2aede591e22be45b368cfe8fa979b2c8d3262c87e82db00d5622ae834027b8b4",
    )

    depends_on("globus-toolkit")
    depends_on("voms")
    depends_on("gsoap")
