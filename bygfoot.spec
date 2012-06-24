Summary:	A simple football manager
Summary(pl):	Prosty menad�er pi�karski
Name:		bygfoot
Version:	1.4.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	7eb56353a62500d7d08c207682e4e27c
URL:		http://bygfoot.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bygfoot is a small and simple football manager game featuring some
international leagues and cups. You manage a team from one such
league: you form the team and buy and sell players.

%description -l pl
Bygfoot jest ma�ym i prostym menad�erem pi�karskim umo�liwiaj�cym gr�
w mi�dzynarodowych ligach i pucharach. Gra polega na tworzeniu dru�yny
oraz kupowaniu i sprzedawaniu zawodnik�w.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
