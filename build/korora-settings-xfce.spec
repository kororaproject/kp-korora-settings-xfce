%define  debug_package %{nil}

Summary:    Korora configs for Xfce
Name:       korora-settings-xfce
Version:    0.11
Release:    4%{?dist}

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
#mkdir -p %{buildroot}%{_libdir}/firefox/browser/defaults/profile
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config

#cp -a %{_builddir}/%{name}-%{version}/prefs-xfce.js %{buildroot}%{_libdir}/firefox/browser/defaults/profile/prefs-xfce.js
cp -a %{_builddir}/%{name}-%{version}/xfce4 %{buildroot}%{_sysconfdir}/skel/.config/

%clean
rm -rf %{buildroot}

%pre

%post
#cd %{_libdir}/firefox/browser/defaults/profile/
#ln -sf prefs-xfce.js prefs.js

%postun
# clean up the link on uninstall of this package (not updates though)
#if [ "$1" == "0" ]
#then
#  cd %{_libdir}/firefox/browser/defaults/profile/
#  unlink prefs.js 2>/dev/null
#  cd -
#fi

%files
%defattr(-,root,root,-)
#%{_libdir}/firefox/browser/defaults/profile/prefs-xfce.js
%{_sysconfdir}/skel/.config/xfce4

%changelog
* Sat Jul 2 2016 Chris Smart <csmart@kororaproject.org> 0.11-4
- Change to Arc theme and Numix Circle icons

* Fri Nov 6 2015 Chris Smart <csmart@kororaproject.org> 0.11-3
- Don't show icons on desktop, enable slideshow background

* Fri Jul 31 2015 Chris Smart <csmart@kororaproject.org> 0.11-2
- Use yumex-dnf instead of yumex

* Fri Jul 24 2015 Ian Firns <firnsy@kororaproject.org> 0.11-1
- Updated whisker menu.

* Wed Jan 04 2015 Chris Smart <csmart@kororaproject.org> 0.10-3
- Update to fix power management icon.

* Sat Dec 27 2014 Chris Smart <csmart@kororaproject.org> 0.10-2
- Update to Whisker menu, updated settings.

* Sat Dec 20 2014 Chris Smart <csmart@kororaproject.org> 0.10-1
- Move firefox profile to generic package.

* Fri Dec 20 2013 Ian Firns <firnsy@kororaproject.org> 0.2-1
- Updated font sizes and removed autohide for bottom panel.

* Tue Nov 19 2013 Chris Smart <csmart@kororaproject.org> 0.1-1
- Initial settings for xfce
