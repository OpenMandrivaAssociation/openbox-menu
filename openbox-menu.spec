%define debug_package %{nil}

Summary:	Dynamic menus in Openbox WM
Name:		openbox-menu
Version:	0.3.6.6
Release:	2
License:	GPLv3
Group:		Graphical desktop/Other
Url:		http://mimarchlinux.googlecode.com/
Source0:	http://mimarchlinux.googlecode.com/%{name}-%{version}.tar.bz2
Patch1:		openbox-menu-0.3.6.6_makefile-install.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libmenu-cache)
Requires:	openbox
Requires:	menu-cache

%description 
An Openbox pipe-menu to display entries in *.desktop files.
 
%prep
%setup -q
%apply_patches

%build
%make

%install
%makeinstall_std

%files 
%doc ChangeLog AUTHORS COPYING
%{_bindir}/%{name}

