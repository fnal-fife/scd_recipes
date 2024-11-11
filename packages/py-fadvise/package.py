# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class PyFadvise(PythonPackage):
    """Interface to POSIX fadvise, since it's not in 'posix'."""

    homepage = "https://chris-lamb.co.uk/projects/python-fadvise"
    pypi = "fadvise/fadvise-6.0.1.tar.gz"

    maintainers("marcmengel", "github_user2")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("BSD-3-Clause-Clear" ) #, checked_by="marcmengel"

    version("6.0.1", sha256="d3122c6b7f59a5f1c7ac628f42766bed0426cab2bff3d28c1f84580d51fb623a")

    with when("^python@3:"):
        patch("fadvise_p3.patch")

    depends_on("python", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
