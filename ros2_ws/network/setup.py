from setuptools import find_packages, setup
import pathlib

package_name = "network"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            "share/" + package_name,
            list(path.as_posix() for path in pathlib.Path("./launch").rglob("*")),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="vscode",
    maintainer_email="jp.ritzenhoff@gmail.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)
