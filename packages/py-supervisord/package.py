# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySupervisord(PythonPackage):
    """Supervisor: A Process Control System

    Supervisor is a client/server system that allows its users to monitor
    and control a number of processes on UNIX-like operating systems.
    """

    homepage = "https://supervisord.org"

    url = "https://pypi.io/packages/source/s/supervisor/supervisor-4.0.3.tar.gz"

    version(
        "4.2.0",
        sha256="64082ebedf6d36ff409ab2878f1aad5c9035f916c5f15a9a1ec7dffc6dfbbed8",
    )
    version(
        "4.0.3",
        sha256="f768abc073e8702892718938b8a0ab98ebcb91c2afcb39bf2cb570d3eb51149e",
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-meld3", type=("build", "run"), when="@:4.1.0")
    depends_on("py-pytest", type="test")
    depends_on("py-pytest-cov", type="test")

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
