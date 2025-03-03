# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyKafka(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/dpkp/kafka-python"
    pypi = "kafka/kafka-1.3.5.tar.gz"

    license("UNKNOWN")

    version("1.3.5", sha256="ffb3348cd918c31344b1a2eb61f692cbc423c83b1b06466a86de3db8a3f6a018")

    depends_on("py-setuptools", type="build")

    def config_settings(self, spec, prefix):
        settings = {}
        return settings
