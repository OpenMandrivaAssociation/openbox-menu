%define debug_package %{nil}
Summary:	Dynamic menus in Openbox WM

Name:		openbox-menu
Version:	0.5.0
Release:	1
License:	GPLv3
Group:		Graphical desktop/Other
URL:		http://mimarchlinux.googlecode.com/
Source0:	http://mimarchlinux.googlecode.com/files/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libmenu-cache)

Requires:	openbox
Requires:	menu-cache

%description 
An Openbox pipe-menu to display entries in *.desktop files.

%prep
%setup -q

%build
%make

%install
%makeinstall_std

%files 
%doc ChangeLog AUTHORS COPYING
/bin/%{name}




