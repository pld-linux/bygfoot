Summary:	A simple football manager
Summary(pl):	Prosty menad¿er pi³karski
Name:		bygfoot
Version:	1.8.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/bygfoot/%{name}-%{version}.tar.bz2
# Source0-md5:	42087e1c0aa581cd25b8885bbc0e2f2a
URL:		http://bygfoot.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bygfoot is a small and simple football manager game featuring some
international leagues and cups. You manage a team from one such
league: you form the team and buy and sell players.

%description -l pl
Bygfoot jest ma³ym i prostym menad¿erem pi³karskim umo¿liwiaj±cym grê
w miêdzynarodowych ligach i pucharach. Gra polega na tworzeniu dru¿yny
oraz kupowaniu i sprzedawaniu zawodników.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/%{name}*
