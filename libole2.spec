Summary:	Structured Storage OLE2 library
Summary(es.UTF-8):   libole2 fornece una API para acessar objetos OLE2
Summary(pl.UTF-8):   Biblioteka obsługująca obiekty OLE2
Summary(pt_BR.UTF-8):   libole2 fornece uma API para acessar objetos OLE2
Summary(ru.UTF-8):   Библиотека структурированного хранения OLE2
Summary(uk.UTF-8):   Бібліотека структурованого зберігання OLE2
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

%description -l es.UTF-8
libole2 fornece una API para acessar objetos OLE2 como é usado nos
componentes da Microsoft. Algunos ejemplos que usan este sistema são
os formatos dos aplicativos Excel, Word, Powerpoint e Visio.

%description -l pl.UTF-8
Bibliotek zawierająca funkcje do obróbki plików OLE2 Structured
Storage. Jest używana przez Gnumerica z GNOME, AbiWorda z AbiSuite
oraz przez inne programy.

%description -l pt_BR.UTF-8
libole2 fornece uma API para acessar objetos OLE2 como é usado nos
componentes da Microsoft. Alguns exemplos que usam este sistema são os
formatos dos aplicativos Excel, Word, Powerpoint e Visio.

%description -l ru.UTF-8
Современные приложения имеют потребность в сохранении множества типов
данных. Один из способов достичь этого - использовать подход "файловая
система внутри файла".

Внутри OLE2 файла есть "потоки" (файлы) и каталоги. Используя libole2
можно легко путешествовать такой файловой системой, создавать,
записывать, читать и удалять в ней файлы, создавать и удалять
каталоги.

%description -l uk.UTF-8
Сучасні прикладні програми мають необхідність зберігати багато типів
даних. Один із способів досягти цього - використовувати підхід
"файлова система всередині файлу".

Всередині OLE2 файлу є "потоки" (файли) та каталоги. Використовуючи
libole2 можна легко подорожувати такою файловою системою, створювати,
записувати, читати та видаляти в ній файли, створювати та видаляти
каталоги.

%package devel
Summary:	Includes etc. to develop libole2 applications
Summary(pl.UTF-8):   Pliki nagłówkowe do tworzenia aplikacji używających libole2
Summary(pt_BR.UTF-8):   Bibliotecas e outros arquivos necessários para desenvolvimento
Summary(ru.UTF-8):   Файлы для разработки приложений, использующих libole2
Summary(uk.UTF-8):   Файли для розробки програм, які користуються libole2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Include files etc. you can use to develop libole2 applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne do tworzenia aplikacji używających libole2.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão necessários para o desenvolvimento
de aplicações baseadas na libole2.

%description devel -l ru.UTF-8
Файлы для разработки приложений, использующих возможности libole2.

%description devel -l uk.UTF-8
Файли для розробки програм, які користуються можливостями libole2.

%package static
Summary:	Libole2 static libraries
Summary(pl.UTF-8):   Statyczne biblioteki libole2
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento com libole2
Summary(ru.UTF-8):   Статические библиотеки для разработки приложений, использующих libole2
Summary(uk.UTF-8):   Статичні бібліотеки для розробки програм, які користуються libole2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Libole2 static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libole2.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libole2

%description static -l ru.UTF-8
Статические библиотеки для разработки приложений, использующих
возможности libole2.

%description static -l uk.UTF-8
Статичні бібліотеки для розробки програм, які користуються
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
