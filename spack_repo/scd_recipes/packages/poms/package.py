from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class Poms(PythonPackage):
    """Production Operations Management System"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://github.com/fermitools/poms"
    url = "https://github.com/fermitools/poms/archive/refs/tags/v4_4_2.tar.gz"

    # FIXME: Add proper versions and checksums here.
    version("4_4_2", sha256="d5b2d602072af08a46343a59d8ecad1c6daec8fd5fb351f8a91eb5164311c2e7")
    version("4_1_2", "8c44623b2fcc78ac2120fb5a185917de")
    version("4_1_0", "c8682135a0d4eae8df00a29ececb6020")
    version("4_2_0", "cf496f78f5e988684d32afa352b0c77b")
    version(
        "4_2_1",
        sha256="baeae29169489dda9be0d5f7ebb9bd93dae2644088a4275a02ede4469d863c28",
    )
    version("4_2_0", "cf496f78f5e988684d32afa352b0c77b")
    version(
        "4_3_0",
        sha256="063a6bac546183cb24fc1ba5228bb640176bc3e9591995a58d39c61aacd6053b",
    )
    version(
        "develop",
        branch="develop",
        git="ssh://p-prod_mgmt_db@cdcvs.fnal.gov/cvs/projects/prod_mgmt_db",
    )

    depends_on("python", type=("build", "run"))
    depends_on("py-cherrypy", type=("build", "run"))
    depends_on("py-future", type=("build", "run"), when="^python@:3.1")
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-more-itertools", type=("build", "run"))
    depends_on("py-prometheus-client", type=("build", "run"))
    depends_on("py-psycopg2", type=("build", "run"))
    depends_on("py-python-crontab", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-sqlalchemy", type=("build", "run"))
    depends_on("data-dispatcher", type=("build", "run"))

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
