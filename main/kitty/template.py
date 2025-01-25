pkgname = "kitty"
pkgver = "0.39.0"
pkgrel = 0
hostmakedepends = [
    "fonts-nerd-symbols-only",
    "go",
    "pkgconf",
    "python-setuptools",
    "wayland-progs",
    "wayland-protocols",
]
makedepends = [
    "dbus-devel",
    "fontconfig-devel",
    "freetype-devel",
    "gettext-devel",
    "harfbuzz-devel",
    "lcms2-devel",
    "libcanberra-devel",
    "libpng-devel",
    "libxcb-devel",
    "libxcursor-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "openssl-devel",
    "python-devel",
    "simde",
    "xxhash-devel",
]
depends = [
    self.with_pkgver("kitty-kitten"),
    self.with_pkgver("kitty-terminfo"),
]
pkgdesc = "Accelerated terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://sw.kovidgoyal.net/kitty"
source = f"https://github.com/kovidgoyal/kitty/releases/download/v{pkgver}/kitty-{pkgver}.tar.xz"
sha256 = "c3f5d2371ce78ae29475d21d31264d41478357024f267d9f6038bb4bcdbc972b"
# nah
options = ["!cross"]

tool_flags = {
    # musl/posix ioctl int argument crap
    "CFLAGS": ["-Wno-error=overflow"],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152"],
}


def prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def build(self):
    from cbuild.util import golang

    self.do(
        "python3",
        "setup.py",
        "linux-package",
        "--ignore-compiler-warnings",
        "--update-check-interval=0",
        "--verbose",
        env=golang.get_go_env(self),
    )


def install(self):
    # nuke pointless optimized pycache
    for f in (self.cwd / "linux-package").rglob("*.opt-*.pyc"):
        f.unlink()
    # install the rest as is
    self.install_files("linux-package", "", name="usr")


@subpackage("kitty-terminfo")
def _(self):
    self.subdesc = "terminfo data"

    return ["usr/share/terminfo"]


@subpackage("kitty-kitten")
def _(self):
    self.subdesc = "kitten client"

    return ["usr/bin/kitten", "usr/share/man/man1/kitten*.1"]
