%define fname	dateutil

Summary:	Provides powerful extensions to the standard datetime module
Name:		python-dateutil
Version:	1.5
Release:	%mkrel 4
License:	Python
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://labix.org/python-dateutil
Source0:	http://labix.org/download/python-dateutil/%{name}-%{version}.tar.bz2
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Requires:	python
BuildArch:	noarch

%description
The dateutil module provides powerful extensions to the standard
datetime module available in Python. Features include:

* Computing of relative deltas (next month, next year, next monday,
  last week of month, etc);
* Computing of relative deltas between two given date and/or datetime
  objects;
* Computing of dates based on very flexible recurrence rules, using a
  superset of the iCalendar specification. Parsing of RFC strings is
  supported as well;
* Generic parsing of dates in almost any string format;
* Timezone (tzinfo) implementations for tzfile(5) format files
  (/etc/localtime, /usr/share/zoneinfo, etc), TZ environment string
  (in all known formats), iCalendar format files, given ranges (with
  help from relative deltas), local machine timezone, fixed offset
  timezone, UTC timezone, and Windows registry-based time zones;
* Internal up-to-date world timezone information based on Olson's
  database;
* Computing of Easter Sunday dates for any given year, using Western,
  Orthodox or Julian algorithms;
* More than 400 test cases.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%post

%postun

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README NEWS
%{py_puresitedir}/%{fname}
%{py_puresitedir}/python_%{fname}-%{version}-py%{py_ver}.egg-info



%changelog
* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 1.5-3mdv2011.0
+ Revision: 672808
- rebuild

* Mon Nov 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.5-2mdv2011.0
+ Revision: 591649
- rebuild for python 2.7

* Sun Apr 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdv2010.1
+ Revision: 531327
- update to new version 1.5

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.4.1-3mdv2010.0
+ Revision: 442092
- rebuild

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 1.4.1-2mdv2009.1
+ Revision: 319472
- rebuild with python 2.6

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.4.1

* Thu Apr 17 2008 Adam Williamson <awilliamson@mandriva.org> 1.4-1mdv2009.0
+ Revision: 195461
- buildrequires python-setuptools
- new release 1.4

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Fri Dec 14 2007 Jérôme Soyer <saispo@mandriva.org> 1.3-1mdv2008.1
+ Revision: 119766
- New release

* Tue Aug 21 2007 Adam Williamson <awilliamson@mandriva.org> 1.2-3mdv2008.0
+ Revision: 68660
- drop manual python-base dependency, there's an auto-generated one

* Tue Aug 21 2007 Adam Williamson <awilliamson@mandriva.org> 1.2-2mdv2008.0
+ Revision: 68590
- add some python requires
- noarch

* Tue Aug 21 2007 Adam Williamson <awilliamson@mandriva.org> 1.2-1mdv2008.0
+ Revision: 68575
- Import python-dateutil

