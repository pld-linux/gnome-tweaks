# TODO: switch to gtk4-update-icon-cache
Summary:	A tool to customize advanced GNOME 3 options
Summary(pl.UTF-8):	Narzędzie do dostosowywania zaawansowanych opcji GNOME 3
Name:		gnome-tweaks
Version:	46.1
Release:	2
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-tweaks/46/%{name}-%{version}.tar.xz
# Source0-md5:	1c770b4db46b037338e0501a6c5cc813
URL:		https://wiki.gnome.org/Apps/Tweaks
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.10
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.78.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.78.0
Requires:	gnome-desktop >= 3.30
Requires:	gnome-settings-daemon
Requires:	gnome-shell >= 3.24
Requires:	gobject-introspection >= 1.78.0
Requires:	gsettings-desktop-schemas >= 46.0
Requires:	gtk4 >= 4.10.0
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.4.0
Requires:	libgudev >= 238
Requires:	libnotify >= 0.7
Requires:	mutter
# Pango-1.0.typelib
Requires:	pango >= 1:1.26
Requires:	python3-pygobject3 >= 3.46.0
Requires:	python3 >= 1:3.10
Requires:	sound-theme-freedesktop
Suggests:	nautilus >= 3.26
Obsoletes:	gnome-tweak-tool < 3.27
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to customize advanced GNOME 3 options.

%description -l pl.UTF-8
Narzędzie do dostosowywania zaawansowanych opcji GNOME 3.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' gnome-tweaks

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}

%ninja_install -C build

# not supported by glibc (as of 2.38)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-tweaks
%{py3_sitescriptdir}/gtweak
%{_datadir}/glib-2.0/schemas/org.gnome.tweaks.gschema.xml
%{_datadir}/gnome-tweaks
%{_datadir}/metainfo/org.gnome.tweaks.appdata.xml
%{_desktopdir}/org.gnome.tweaks.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.tweaks.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.tweaks-symbolic.svg
