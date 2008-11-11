Summary:	GNOME solution for scanning
Name:		gnome-scan
Version:	0.6
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-scan/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	4bdf2d0ce27893aa802743d24b853afd
URL:		http://www.gnome.org/projects/gnome-scan/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gegl-devel >= 0.0.16
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel >= 2.3
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	intltool >= 0.36.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sane-backends-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Scan provide a library for use by applications (e.g. using
plugins) as well as a tiny standalone application, called flegita,
which allow to simply save scan to file.

%package libs
Summary:	gnomescan library
Summary(pl.UTF-8):	Biblioteka gnomescan
Group:		X11/Libraries

%description libs
gnomescan library.

%description libs -l pl.UTF-8
Biblioteka gnomescan.

%package devel
Summary:	Header files for gnomescan library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gnomescan
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gegl-devel >= 0.0.16
Requires:	gimp-devel >= 2.3

%description devel
Header files for gnomescan library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gnomescan.

%package static
Summary:	Static gnomescan library
Summary(pl.UTF-8):	Statyczna biblioteka gnomescan
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gnomescan library.

%description static -l pl.UTF-8
Statyczna biblioteka gnomescan.

%package apidocs
Summary:	gnomescan library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gnomescan
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gnomescan library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gnomescan.

%package -n gimp-plugin-flegita
Summary:	flegita plugin for GIMP
Summary(pl.UTF-8):	Wtyczka flegita dla GIMPa
Group:		X11/Applications/Graphics
# for icons
Requires:	%{name} = %{version}-%{release}

%description -n gimp-plugin-flegita
flegita plugin for GIMP.

%description -n gimp-plugin-flegita -l pl.UTF-8
Wtyczka flegita dla GIMPa.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-scan-1.0/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/flegita
%{_datadir}/gnome-scan
%{_desktopdir}/flegita.desktop
%{_iconsdir}/hicolor/*/*/*.svg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomescan.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomescan.so.0
%dir %{_libdir}/gnome-scan-1.0
%attr(755,root,root) %{_libdir}/gnome-scan-1.0/libgsane.so
%attr(755,root,root) %{_libdir}/gnome-scan-1.0/libgsfiles.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomescan.so
%{_libdir}/libgnomescan.la
%{_includedir}/gnome-scan-1.0
%{_pkgconfigdir}/gnome-scan.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomescan.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnome-scan-1.0

%files -n gimp-plugin-flegita
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/2.0/plug-ins/flegita-gimp
