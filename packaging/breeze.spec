# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       breeze

# >> macros
# << macros

Summary:    Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
Version:    5.1.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  breeze.yaml
Source101:  breeze-rpmlintrc
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcompletion-devel
BuildRequires:  frameworkintegration-devel
BuildRequires:  kwindowsystem-devel

%description
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.


%package kde4
Summary:    KDE 4 settings for the "Breeze" theme
Group:      System/Base

%description kde4
This package contains KDE 4 settings for the "Breeze" theme.


%package icon-theme
Summary:    Breeze icon theme
Group:      System/Base
BuildArch:  noarch
Requires:   oxygen-icon-theme

%description icon-theme
Breeze is the standard icon theme for Plasma, but follows the freedesktop.org
icon schemes, so it can be used in other desktop environments using this
specification.


%package cursor-theme
Summary:    Breeze cursor theme
Group:      System/Base
BuildArch:  noarch

%description cursor-theme
A full set of cursors for the Breeze visual style.


%package kwin
Summary:    KWin "Breeze" decoration
Group:      System/Base
BuildArch:  noarch
Requires:   kwin

%description kwin
This package contains the "Breeze" decoration for KWin.


%package style
Summary:    QtQuickControls "Breeze" style
Group:      System/Base
BuildArch:  noarch
Requires:   qt5-qtquickcontrols

%description style
This package contains the "Breeze" style for QtQuickControls.


%package kstyle
Summary:    QtWidgets "Breeze" style
Group:      System/Base

%description kstyle
This package contains the "Breeze" style for QtWidgets.


%package color-schemes
Summary:    Breeze color schemes
Group:      System/Base
BuildArch:  noarch

%description color-schemes
This package contains the "Breeze" color schemes.


%package qtcurve
Summary:    QtCurve "Breeze" theme
Group:      System/Base
BuildArch:  noarch
Requires:   qtcurve-qt5

%description qtcurve
This package contains the "Breeze" theme for QtCurve.


%package wallpapers
Summary:    Breeze wallpapers
Group:      System/Base
BuildArch:  noarch

%description wallpapers
This package contains wallpapers from the "Breeze" visual style.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post


%files kde4
%defattr(-,root,root,-)
%{_kf5_libdir}/kconf_update_bin/*
%{_kf5_sharedir}/kconf_update/*
# >> files kde4
# << files kde4

%files icon-theme
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_kf5_sharedir}/icons/breeze*
%{_kf5_sharedir}/icons/breeze-dark/*
# >> files icon-theme
# << files icon-theme

%files cursor-theme
%defattr(-,root,root,-)
%doc cursors/src/README COPYING AUTHORS
%{_kf5_sharedir}/icons/breeze_cursors/*
# >> files cursor-theme
# << files cursor-theme

%files kwin
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_kf5_servicesdir}/kwin/*
%{_kf5_sharedir}/kwin/decorations/*
# >> files kwin
# << files kwin

%files style
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_kf5_qmldir}/QtQuick/Controls/Styles/Breeze/*
# >> files style
# << files style

%files kstyle
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_kf5_sharedir}/kstyle/*
%{_kf5_plugindir}/kstyle_*
%{_kf5_plugindir}/styles/*
# >> files kstyle
# << files kstyle

%files color-schemes
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_kf5_sharedir}/color-schemes/*
# >> files color-schemes
# << files color-schemes

%files qtcurve
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_kf5_sharedir}/QtCurve/*
# >> files qtcurve
# << files qtcurve

%files wallpapers
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_kf5_sharedir}/wallpapers/*
# >> files wallpapers
# << files wallpapers
