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
#     spack install py-python-crontab
#
# You can edit this file again by typing:
#
#     spack edit py-python-crontab
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPythonCrontab(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://gitlab.com/doctormo/python-crontab/"
    url = "https://pypi.io/packages/source/p/python-crontab/python-crontab-2.5.1.tar.gz"

    maintainers = ["marc.mengel@gmail.com"]

    version(
        "2.5.1",
        sha256="4bbe7e720753a132ca4ca9d4094915f40e9d9dc8a807a4564007651018ce8c31",
    )

    depends_on("python", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    def build_args(self, spec, prefix):
        args = []
        return args
