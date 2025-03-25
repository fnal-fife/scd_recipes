# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Rucio(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://rucio.cern.ch"
    pypi = "rucio/rucio-1.30.0.tar.gz"

    # maintainers = ["marcmengel","bari12"]

    version("1.30.0", sha256="088c962dbd9e86546ea8889c88b3555d5c55ac57cca485fb5027806eb1732432")

    variant("client-only", default=True)

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-pip", type="build")

    depends_on("py-requests", type=("build", "run"))
    depends_on("py-urllib3", type=("build", "run"))
    depends_on("py-dogpile.cache", type=("build", "run"))
    depends_on("py-tabulate", type=("build", "run"))
    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-paramiko", type=("build", "run"))
    depends_on("py-kerberos", type=("build", "run"))
    depends_on("py-requests-kerberos", type=("build", "run"))
    depends_on("py-python-swiftclient", type=("build", "run"))
    depends_on("py-argcomplete", type=("build", "run"))
    depends_on("py-python-magic", type=("build", "run"))
    depends_on("py-sqlalchemy", type=("build", "run"))
    depends_on("py-alembic", type=("build", "run"))
    depends_on("py-pymemcache", type=("build", "run"))
    depends_on("py-python-dateutil", type=("build", "run"))
    depends_on("py-stomp.py", type=("build", "run"))
    depends_on("py-statsd", type=("build", "run"))
    depends_on("py-geoip2", type=("build", "run"))
    depends_on("py-google-auth", type=("build", "run"))
    depends_on("py-redis", type=("build", "run"))
    depends_on("py-flask", type=("build", "run"))
    depends_on("py-oic", type=("build", "run"))
    depends_on("py-prometheus_client", type=("build", "run"))
    depends_on("py-boto3", type=("build", "run"))
    depends_on("py-cx_oracle", type=("build", "run"))
    depends_on("py-psycopg2-binary", type=("build", "run"))
    depends_on("py-pymysql", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-globus-sdk", type=("build", "run"))
    depends_on("py-python3-saml", type=("build", "run"))
    depends_on("py-pymongo", type=("build", "run"))
