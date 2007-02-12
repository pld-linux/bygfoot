Summary:	A simple football manager
Summary(pl.UTF-8):	Prosty menadżer piłkarski
Name:		bygfoot
Version:	2.1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/bygfoot/%{name}-%{version}-source.tar.bz2
# Source0-md5:	001790f36d0d3b706c8d39176363ee2f
Source1:	%{name}.desktop
URL:		http://bygfoot.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bygfoot is a small and simple football manager game featuring some
international leagues and cups. You manage a team from one such
league: you form the team and buy and sell players.

%description -l pl.UTF-8
Bygfoot jest małym i prostym menadżerem piłkarskim umożliwiającym grę
w międzynarodowych ligach i pucharach. Gra polega na tworzeniu drużyny
oraz kupowaniu i sprzedawaniu zawodników.

%prep
%setup -q -n %{name}-%{version}-source

%build
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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}_icon.png
