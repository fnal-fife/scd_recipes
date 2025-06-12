# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyCondb2(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/fermisda/condb2"
    git = "https://github.com/fermisda/condb2.git"
    url = "https://github.com/fermisda/condb2/archive/refs/tags/2.1.4.tar.gz"

    # maintainers("github_user1", "github_user2")

    license("BSD 3-Clause")

    version("main", branch="main")
    version("develop", branch="develop")
    version("2.1.4", sha256="81182ebb85debbf3bc82abed31ee9338a942bd51260bb3709c7618fe6e797161")
    version("2.1.2", sha256="1724b1bfac00db7b2683162094e2c337a902696104d25b891773a3008fc8d814")
    version("2.1.1", sha256="a0d560b5e22eda9470782e2a2d9b57bd48f138e811a964214919baf9ce040604")
    version("2.1.0", sha256="c44140e08d84358c33946d3110afe3337e2f82978ba44d6bec41ac5a1f788e14")
    version("2.0.3", sha256="f11913817fa440def2bb5e6636d47289ee286ede7ee409e0372ce6678e6b93e1")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
    depends_on("py-psycopg2")

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
