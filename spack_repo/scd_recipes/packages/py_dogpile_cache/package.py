# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyDogpileCache(PythonPackage):
    """cache package based on dogpile locks"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/sqlalchemy/dogpile.cache"
    pypi = "dogpile.cache/dogpile.cache-1.1.8.tar.gz"

    maintainers = [
        "marcmengel",
    ]

    version("1.2.2", sha256="fd9022c0d9cbadadf20942391a95adaf296be80b42daa8e202f8de1c21f198b2")
    version("1.1.8", sha256="d844e8bb638cc4f544a4c89a834dfd36fe935400b71a16cbd744ebdfb720fd4e")

    depends_on("py-setuptools", type="build")

    depends_on("py-decorator", type=("build", "run"))
    depends_on("py-stevedore", type=("build", "run"))
