Name:           media-player-info
Version:        6
Release:        1%{?dist}
Summary:        Data files describing media player capabilities

Group:          System Environment/Base
License:        BSD
URL:            http://cgit.freedesktop.org/~teuf/media-player-id/
Source0:        http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  libudev-devel
Requires:       udev

%description
media-player-info is a repository of data files describing media player
(mostly USB Mass Storage ones) capabilities. These files contain information
about the directory layout to use to add music to these devices, about the
supported file formats, etc.

The package also installs a udev rule to identify media player devices.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING README NEWS AUTHORS
%{_datadir}/media-player-info
/lib/udev/rules.d/*


%changelog
* Fri May 14 2010 Matthias Clasen <mclasen@redhat.com> - 6-1
- Fix the source URL
- Use a newer upstream release with support for many more media players
Resolves: #592310

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3-1.1
- Rebuilt for RHEL 6

* Tue Sep  1 2009 Matthias Clasen <mclasen@redhat.com> - 3-1
- New upstream tarball with fixed Copyright headers

* Sat Aug 29 2009 Matthias Clasen <mclasen@redhat.com> - 2-1
- Rename to media-player-info

* Thu Aug 27 2009 Matthias Clasen <mclasen@redhat.com> - 1-1
- Initial packaging
