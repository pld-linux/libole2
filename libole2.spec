Summary:	Structured Storage OLE2 library
Summary(es):	libole2 fornece una API para acessar objetos OLE2
Summary(pl):	Biblioteka obsЁuguj╠ca obiekty OLE2
Summary(pt_BR):	libole2 fornece uma API para acessar objetos OLE2
Summary(ru):	Библиотека структурированного хранения OLE2
Summary(uk):	Б╕бл╕отека структурованого збер╕гання OLE2
Name:		libole2
Version:	2.2.8
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libole2/2.2/%{name}-%{version}.tar.bz2
Patch0:		%{name}-acfix.patch
# Source0-md5:	0db6170f45795bf3e34f12d52bb598a1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1.3.10
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library containing functionality to manipulate OLE2 Structured
Storage files. It is used by Gnumeric from GNOME, AbiWord from
AbiSuite and by other programs.

%description -l es
libole2 fornece una API para acessar objetos OLE2 como И usado nos
componentes da Microsoft. Algunos ejemplos que usan este sistema sЦo
os formatos dos aplicativos Excel, Word, Powerpoint e Visio.

%description -l pl
Bibliotek zawieraj╠ca funkcje do obrСbki plikСw OLE2 Structured
Storage. Jest u©ywana przez Gnumerica z GNOME, AbiWorda z AbiSuite
oraz przez inne programy.

%description -l pt_BR
libole2 fornece uma API para acessar objetos OLE2 como И usado nos
componentes da Microsoft. Alguns exemplos que usam este sistema sЦo os
formatos dos aplicativos Excel, Word, Powerpoint e Visio.

%description -l ru
Современные приложения имеют потребность в сохранении множества типов
данных. Один из способов достичь этого - использовать подход "файловая
система внутри файла".

Внутри OLE2 файла есть "потоки" (файлы) и каталоги. Используя libole2
можно легко путешествовать такой файловой системой, создавать,
записывать, читать и удалять в ней файлы, создавать и удалять
каталоги.

%description -l uk
Сучасн╕ прикладн╕ програми мають необх╕дн╕сть збер╕гати багато тип╕в
даних. Один ╕з способ╕в досягти цього - використовувати п╕дх╕д
"файлова система всередин╕ файлу".

Всередин╕ OLE2 файлу ╓ "потоки" (файли) та каталоги. Використовуючи
libole2 можна легко подорожувати такою файловою системою, створювати,
записувати, читати та видаляти в н╕й файли, створювати та видаляти
каталоги.

%package devel
Summary:	Includes etc. to develop libole2 applications
Summary(pl):	Pliki nagЁСwkowe do tworzenia aplikacji u©ywaj╠cych libole2
Summary(pt_BR):	Bibliotecas e outros arquivos necessАrios para desenvolvimento
Summary(ru):	Файлы для разработки приложений, использующих libole2
Summary(uk):	Файли для розробки програм, як╕ користуються libole2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Include files etc. you can use to develop libole2 applications.

%description devel -l pl
Pliki nagЁСwkowe i inne do tworzenia aplikacji u©ywaj╠cych libole2.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusЦo necessАrios para o desenvolvimento
de aplicaГУes baseadas na libole2.

%description devel -l ru
Файлы для разработки приложений, использующих возможности libole2.

%description devel -l uk
Файли для розробки програм, як╕ користуються можливостями libole2.

%package static
Summary:	Libole2 static libraries
Summary(pl):	Statyczne biblioteki libole2
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com libole2
Summary(ru):	Статические библиотеки для разработки приложений, использующих libole2
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки програм, як╕ користуються libole2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Libole2 static libraries.

%description static -l pl
Statyczne biblioteki libole2.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com libole2

%description static -l ru
Статические библиотеки для разработки приложений, использующих
возможности libole2.

%description static -l uk
Статичн╕ б╕бл╕отеки для розробки програм, як╕ користуються
можливостями libole2.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libole2-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
