Summary:    Korora configs for Xfce
Name:       korora-settings-xfce
Version:    0.2
Release:    1%{?dist}.1

Group:      System Environment/Base
License:    GPLv3+
Url:        http://kororaproject.org
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildArch: noarch

%description
%{summary}.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/firefox/browser/defaults/profile
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config

cp -a %{_builddir}/%{name}-%{version}/prefs-xfce.js %{buildroot}%{_libdir}/firefox/browser/defaults/profile/prefs-xfce.js
cp -a %{_builddir}/%{name}-%{version}/xfce4 %{buildroot}%{_sysconfdir}/skel/.config/

%clean
rm -rf %{buildroot}

%pre

%post
cd %{_libdir}/firefox/browser/defaults/profile/
ln -sf prefs-xfce.js prefs.js

%postun
# clean up the link on uninstall of this package (not updates though)
if [ "$1" == "0" ]
then
  cd %{_libdir}/firefox/browser/defaults/profile/
  unlink prefs.js 2>/dev/null
  cd -
fi

%files
%defattr(-,root,root,-)
%{_libdir}/firefox/browser/defaults/profile/prefs-xfce.js
%{_sysconfdir}/skel/.config/xfce4

%changelog
* Fri Dec 20 2013 Ian Firns <firnsy@kororaproject.org> 0.2-1
- Updated font sizes and removed autohide for bottom panel.

* Tue Nov 19 2013 Chris Smart <csmart@kororaproject.org> 0.1-1
- Initial settings for xfce
