Summary:	Structured Storage OLE2 library
Name:		libole2
Version:	0.1.7
Release:	1
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/libole2/%{name}-%{version}.tar.gz
BuildRequires:	glib-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A library containing functionality to manipulate OLE2 Structured
Storage files. It is used by Gnumeric from Gnome, AbiWord from
AbiSuite and by other programs.

%package devel
Summary:	Libraries, includes, etc to develop libole2 applications
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop libole2
applications.

%package static
Summary:	Libole2 static libraries
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description static
Libole2 static libraries.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README \
	doc/{*txt,html/*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/{*txt,html/*}.gz
%attr(755,root,root) %{_bindir}/libole2-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/*.sh
%{_aclocaldir}/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
