pkgname = "keditbookmarks"
pkgver = "24.08.2"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kbookmarks-devel",
    "kcodecs-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kparts-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libx11-devel",
    "qt6-qtbase-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE bookmarks editor"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
url = "https://github.com/KDE/keditbookmarks"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/keditbookmarks-{pkgver}.tar.xz"
)
sha256 = "d2c82f5df5801ec6df138d10460e94ec383eefd3b5759ecb63442d92e403c005"
