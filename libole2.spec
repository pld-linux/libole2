Summary:	Structured Storage OLE2 library
Summary(es):	libole2 fornece una API para acessar objetos OLE2
Summary(pt_BR):	libole2 fornece uma API para acessar objetos OLE2
Name:		libole2
Version:	0.2.4
Release:	2
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/libole2/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library containing functionality to manipulate OLE2 Structured
Storage files. It is used by Gnumeric from Gnome, AbiWord from
AbiSuite and by other programs.

%description -l es
libole2 fornece una API para acessar objetos OLE2 como È usado nos
componentes da Microsoft. Algunos ejemplos que usan este sistema s„o
os formatos dos aplicativos Excel, Word, Powerpoint e Visio.

%description -l pt_BR
libole2 fornece uma API para acessar objetos OLE2 como È usado nos
componentes da Microsoft. Alguns exemplos que usam este sistema s„o os
formatos dos aplicativos Excel, Word, Powerpoint e Visio.

%package devel
Summary:	Libraries, includes, etc to develop libole2 applications
Summary(es):	Libraries, includes, etc to develop libole2 applications
Summary(pt_BR):	Bibliotecas e outros arquivos necess·rios para desenvolvimento
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop libole2
applications.

%description -l es devel
Libraries, include files, etc you can use to develop libole2
applications.

%description -l pt_BR devel
Bibliotecas e arquivos de inclus„o necess·rios para o desenvolvimento
de aplicaÁıes baseadas na libole2.

%package static
Summary:	Libole2 static libraries
Summary(es):	Static libraries for libole2 development
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com libole2
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Libole2 static libraries.

%description -l es static
Static libraries for libole2 development

%description -l pt_BR static
Bibliotecas est·ticas para desenvolvimento com libole2

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libole2aclocaldir=%{_aclocaldir}

gzip -9nf README doc/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/{*.txt.gz,html/*}
%attr(755,root,root) %{_bindir}/libole2-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/libole2Conf.sh
%{_aclocaldir}/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
