%define major 1
%define libname %mklibname xpresent %{major}
%define devname %mklibname xpresent -d

Name: libxpresent
Version: 1.0.0
Release: 2
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXpresent-%{version}.tar.bz2
Summary: An Xlib compatible API for the Present extension
URL: http://xorg.freedesktop.org/
License: MIT
Group: System/Libraries
BuildRequires: x11-proto-devel
BuildRequires: x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: gettext
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(presentproto)
BuildRequires: pkgconfig(xextproto)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xrandr)

%description
An Xlib compatible API for the Present extension

%package -n %{libname}
Summary: An Xlib compatible API for the Present extension
Group: System/Libraries

%description -n %{libname}
An Xlib compatible API for the Present extension

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -n libXpresent-%{version} -p1

%build
%configure
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*.3*
