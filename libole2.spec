Summary:	Structured Storage OLE2 library
Summary(es):	libole2 fornece una API para acessar objetos OLE2
Summary(pl):	Biblioteka obs≥uguj±ca obiekty OLE2
Summary(pt_BR):	libole2 fornece uma API para acessar objetos OLE2
Name:		libole2
Version:	0.2.4
Release:	4
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

%description -l pl
Bibliotek zawieraj±ca funkcje do obrÛbki plikÛw OLE2 Structured
Storage. Jest uøywana przez Gnumerica z GNOME, AbiWorda z AbiSuite
oraz przez inne programy.

%description -l pt_BR
libole2 fornece uma API para acessar objetos OLE2 como È usado nos
componentes da Microsoft. Alguns exemplos que usam este sistema s„o os
formatos dos aplicativos Excel, Word, Powerpoint e Visio.

%package devel
Summary:	Includes etc. to develop libole2 applications
Summary(pl):	Pliki nag≥Ûwkowe do tworzenia aplikacji uøywaj±cych libole2
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
Include files etc. you can use to develop libole2 applications.

%description devel -l pl
Pliki nag≥Ûwkowe i inne do tworzenia aplikacji uøywaj±cych libole2.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus„o necess·rios para o desenvolvimento
de aplicaÁıes baseadas na libole2.

%package static
Summary:	Libole2 static libraries
Summary(pl):	Statyczne biblioteki libole2
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

%description static -l pl
Statyczne biblioteki libole2.

%description static -l pt_BR
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
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/lib
# that's where gnome-config will be looking for it
mv $RPM_BUILD_ROOT%{_libdir}/libole2Conf.sh $RPM_BUILD_ROOT%{_prefix}/X11R6/lib
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
%{_prefix}/X11R6/lib/libole2Conf.sh
%{_aclocaldir}/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
