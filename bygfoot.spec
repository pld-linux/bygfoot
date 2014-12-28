Summary:	A simple football manager
Summary(hu.UTF-8):	Egy football menedzser játék
Summary(pl.UTF-8):	Prosty menadżer piłkarski
Name:		bygfoot
Version:	2.3.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/bygfoot/%{name}-%{version}.tar.bz2
# Source0-md5:	152c0c729c2b5e4428d32b89edc6dd14
Source1:	%{name}.desktop
Patch0:		%{name}-locale_names.patch
URL:		http://bygfoot.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	freetype-devel
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bygfoot is a small and simple football manager game featuring some
international leagues and cups. You manage a team from one such
league: you form the team and buy and sell players.

%description -l hu.UTF-8
Bygfoot egy kicsi és egyszerű football menedzser játék, néhány
nemzetközi ligával és kupával. Te menedzseled a csapatot egy
ligában: te alakítod a csapatot, eladhatsz és vehetsz
játékosokat.

%description -l pl.UTF-8
Bygfoot jest małym i prostym menadżerem piłkarskim umożliwiającym
grę w międzynarodowych ligach i pucharach. Gra polega na tworzeniu
drużyny oraz kupowaniu i sprzedawaniu zawodników.

%prep
%setup -q
%patch0 -p1

mv po/zh{,_CN}.po
mv po/pt{_PT,}.po

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install support_files/pixmaps/bygfoot_icon.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO UPDATE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}_icon.png
