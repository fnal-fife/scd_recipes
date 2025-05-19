from spack.package import *


class PyMeld3(PythonPackage):
    """meld3 is an HTML/XML templating system for Python"""

    homepage = "https://github.com/supervisor/meld3"
    url = "https://pypi.io/packages/source/m/meld3/meld3-1.0.2.tar.gz"

    version(
        "2.0.1",
        sha256="3ea266994f1aa83507679a67b493b852c232a7905e29440a6b868558cad5e775",
    )
    version(
        "1.0.2",
        sha256="f7b754a0fde7a4429b2ebe49409db240b5699385a572501bb0d5627d299f9558",
    )

    depends_on("py-setuptools", type="build")
