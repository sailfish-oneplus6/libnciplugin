Name: libnciplugin
Version: 1.0.2
Release: 0
Summary: Support library for NCI-based nfcd plugins
Group: Development/Libraries
License: BSD
URL: https://github.com/mer-hybris/libnciplugin
Source: %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libncicore)
BuildRequires:  pkgconfig(libglibutil)
BuildRequires: pkgconfig(nfcd-plugin) >= 1.0.25
Requires: nfcd >= 1.0.20
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Provides basic functionality for NCI-based nfcd plugins.

%package devel
Summary: Development library for %{name}
Requires: %{name} = %{version}
Requires: pkgconfig

%description devel
This package contains the development library for %{name}.

%prep
%setup -q

%build
make KEEP_SYMBOLS=1 release pkgconfig

%install
rm -rf %{buildroot}
make install-dev DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}.so
%{_includedir}/nciplugin/*.h
