%define fname	dateutil

Summary:	Provides powerful extensions to the standard datetime module
Name:		python-dateutil
Version:	1.4.1
Release:	%{mkrel 2}
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
%{py_puresitedir}/python_%{fname}-%{version}-py%{pyver}.egg-info

