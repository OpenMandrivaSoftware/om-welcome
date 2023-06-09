Name:		om-welcome
Version:	2.5.3
Release:	1
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaAssociation/oma-welcome
Source0:	%{name}-%version.tar.gz
#Source0:
Requires:	kdialog
Requires:	htmlscript >= 1.0.1
BuildRequires:	make
BuildArch:	noarch
%rename oma-welcome

%description
Introduce new users to the OpenMandriva Lx.

%prep
%setup -q
%autopatch -p1

%build
# Nothing to do here...

%install
%makeinstall_std

%find_lang om-welcome

%files -f om-welcome.lang
%{_sysconfdir}/xdg/autostart/om-welcome.desktop
%{_bindir}/enable-repo
%{_bindir}/disable-repo
%{_bindir}/om-welcome
%{_bindir}/om-welcome-launcher
%{_datadir}/%{name}/*
%{_datadir}/applications/om-welcome.desktop
