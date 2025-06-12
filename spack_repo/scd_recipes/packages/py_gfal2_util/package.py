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
#     spack install py-gfal2-util
#
# You can edit this file again by typing:
#
#     spack edit py-gfal2-util
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyGfal2Util(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://gitlab.cern.ch/dmc/"
    url = "https://gitlab.cern.ch/dmc/gfal2-util/-/archive/v1.3.0/gfal2-util-v1.3.0.tar.bz2"

    maintainers = [
        "marcmengel",
    ]

    version(
        "1.6.0-rc1",
        sha256="3c0b2df6761a1e439857cf9f1274cfb4762985b436da308fc03fe1b1231cfcf3",
    )
    version(
        "1.6.0",
        sha256="8c21d3fa824d3583a6c310e8abebbb611b53a754e49f046d28fedc308fb19fae",
    )
    version(
        "1.5.4",
        sha256="0d7e8fb88ce9b99b9b70c26770e50c28a1a8d80bf002ef2fe12b267283181494",
    )
    version(
        "1.5.3",
        sha256="1507f3aa201614319436fff2fdf821856f19a7ffd6c67260b8d8bbcafdf32228",
    )

    depends_on("python", type=("build", "run"))
    # depends_on('py-setuptools', type='build')
    depends_on("gfal2-python", type=("build", "run"))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
