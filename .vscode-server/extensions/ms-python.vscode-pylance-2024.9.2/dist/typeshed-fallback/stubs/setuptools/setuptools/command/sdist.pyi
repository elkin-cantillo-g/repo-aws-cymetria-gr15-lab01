from _typeshed import Incomplete
from typing import ClassVar

from .._distutils.command import sdist as orig

def walk_revctrl(dirname: str = "") -> None: ...

class sdist(orig.sdist):
    user_options: ClassVar[list[tuple[str, str | None, str]]]
    negative_opt: ClassVar[dict[str, str]]
    README_EXTENSIONS: ClassVar[list[str]]
    READMES: ClassVar[tuple[str, ...]]
    filelist: Incomplete
    def run(self) -> None: ...
    def initialize_options(self) -> None: ...
    def make_distribution(self) -> None: ...
    def check_readme(self) -> None: ...
    def make_release_tree(self, base_dir, files) -> None: ...
    def read_manifest(self) -> None: ...
