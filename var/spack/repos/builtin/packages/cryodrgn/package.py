# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cryodrgn(PythonPackage):
    """CryoDRGN is a neural network based algorithm for heterogeneous cryo-EM reconstruction.
    In particular, the method models a continuous distribution over 3D structures by using a
    neural network based representation for the volume"""

    homepage = "https://cryodrgn.cs.princeton.edu/"
    pypi = "cryodrgn/cryodrgn-2.3.0.tar.gz"

    license("GPL-3.0-only", checked_by="A-N-Other")

    version("2.3.0", sha256="9dd75967fddfa56d6b2fbfc56933c50c9fb994326112513f223e8296adbf0afc")

    depends_on("py-setuptools@61:", type="build")
    depends_on("py-setuptools-scm@6.2:", type="build")

    depends_on("py-torch@1:", type=("build", "run"))
    depends_on("py-pandas@:2", type=("build", "run"))
    depends_on("py-numpy@:1.23", type=("build", "run"))
    depends_on("py-matplotlib@:3.7", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-scipy@1.3.1:", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-seaborn@:0.12", type=("build", "run"))
    depends_on("py-cufflinks", type=("build", "run"))
    depends_on("py-jupyterlab", type=("build", "run"))
    depends_on("py-notebook@:7", type=("build", "run"))
    depends_on("py-umap-learn", type=("build", "run"))
    depends_on("py-ipywidgets@:8", type=("build", "run"))
    depends_on("py-healpy", type=("build", "run"))
