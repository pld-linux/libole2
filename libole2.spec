Summary:	Structured Storage OLE2 library
Summary(es):	libole2 fornece una API para acessar objetos OLE2
Summary(pl):	Biblioteka obs³uguj±ca obiekty OLE2
Summary(pt_BR):	libole2 fornece uma API para acessar objetos OLE2
Name:		libole2
Version:	0.2.4
Release:	4
License:	GPL
Group:		Development/Libraries
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
libole2 fornece una API para acessar objetos OLE2 como é usado nos
componentes da Microsoft. Algunos ejemplos que usan este sistema são
os formatos dos aplicativos Excel, Word, Powerpoint e Visio.

%description -l pl
Bibliotek zawieraj±ca funkcje do obróbki plików OLE2 Structured
Storage. Jest u¿ywana przez Gnumerica z GNOME, AbiWorda z AbiSuite
oraz przez inne programy.

%description -l pt_BR
libole2 fornece uma API para acessar objetos OLE2 como é usado nos
componentes da Microsoft. Alguns exemplos que usam este sistema são os
formatos dos aplicativos Excel, Word, Powerpoint e Visio.

%package devel
Summary:	Includes etc. to develop libole2 applications
Summary(pl):	Pliki nag³ówkowe do tworzenia aplikacji u¿ywaj±cych libole2
Summary(pt_BR):	Bibliotecas e outros arquivos necessários para desenvolvimento
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description devel
Include files etc. you can use to develop libole2 applications.

%description devel -l pl
Pliki nag³ówkowe i inne do tworzenia aplikacji u¿ywaj±cych libole2.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão necessários para o desenvolvimento
de aplicações baseadas na libole2.

%package static
Summary:	Libole2 static libraries
Summary(pl):	Statyczne biblioteki libole2
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com libole2
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}

%description static
Libole2 static libraries.

%description static -l pl
Statyczne biblioteki libole2.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com libole2

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
%{_datadir}/libole2

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/{*.txt.gz,html/*}
%attr(755,root,root) %{_bindir}/libole2-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/libole2Conf.sh
%{_aclocaldir}/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
