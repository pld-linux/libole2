Summary: Structured Storage OLE2 library
Name: libole2
Version: 0.1.6
Release: 1
Group: Development/Libraries
Copyright: GPL
Source: ftp://ftp.gnome.org/pub/GNOME/unstable/sources/libole2/%{name}-%{version}.tar.gz
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root

%description
A library containing functionality to manipulate OLE2 Structured Storage files. It is used by Gnumeric from Gnome, AbiWord from AbiSuite and by other programs.

%package devel
Summary: Libraries, includes, etc to develop libole2 applications
Group: X11/Libraries
Requires: libole2

%description devel
Libraries, include files, etc you can use to develop libole2 applications.

%package static
Summary:	Static libraries
Group: X11/Libraries
Requires: libole2-devel

%description static

%prep

%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
make prefix=$RPM_BUILD_ROOT%{_prefix} libdir=$RPM_BUILD_ROOT%{_libdir} \
  includedir=$RPM_BUILD_ROOT%{_includedir} \
  datadir=$RPM_BUILD_ROOT%{_datadir} \
  bindir=$RPM_BUILD_ROOT%{_bindir} \
  install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/lib*.so.*
%{_datadir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libole2-config
%{_libdir}/lib*.so
%{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*a

%changelog
* Wed Jun 28 2000 Arturo Tena <arturo@directmail.org>
- Updated summary and description.
* Sun May 23 2000 John Gotts <jgotts@linuxsavvy.com>
- New SPEC file.
