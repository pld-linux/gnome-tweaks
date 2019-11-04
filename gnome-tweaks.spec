Summary:	A tool to customize advanced GNOME 3 options
Summary(pl.UTF-8):	Narzędzie do dostosowywania zaawansowanych opcji GNOME 3
Name:		gnome-tweaks
Version:	3.34.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tweaks/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	a625d8b167c5549c68e1c6ac7a87d369
URL:		https://wiki.gnome.org/action/show/Apps/Tweaks
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.24
BuildRequires:	intltool >= 0.40.0
BuildRequires:	meson >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	python-pygobject3-devel >= 3.10
BuildRequires:	python3 >= 1:3.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	gnome-desktop >= 3.8.0
Requires:	gnome-shell >= 3.8.0
Requires:	gobject-introspection
Requires:	gsettings-desktop-schemas >= 3.24
Requires:	gtk+3 >= 3.12.0
Requires:	hicolor-icon-theme
Requires:	libnotify >= 0.7
Requires:	libsoup >= 2.4
Requires:	python-pygobject3 >= 3.10
Requires:	python3 >= 1:3.0
Obsoletes:	gnome-tweak-tool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to customize advanced GNOME 3 options.

%description -l pl.UTF-8
Narzędzie do dostosowywania zaawansowanych opcji GNOME 3.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python,/usr/bin/python,' gnome-tweaks gnome-tweak-tool-lid-inhibitor

%build
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/gnome-tweaks
%attr(755,root,root) %{_libexecdir}/gnome-tweak-tool-lid-inhibitor
%{py3_sitedir}/gtweak
%{_datadir}/gnome-tweaks
%{_datadir}/metainfo/org.gnome.tweaks.appdata.xml
%{_desktopdir}/org.gnome.tweaks.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.tweaks.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.tweaks-symbolic.svg
