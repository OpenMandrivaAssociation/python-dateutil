%define fname	dateutil

Summary:	Provides powerful extensions to the standard datetime module
Name:		python-dateutil
Version:	2.6.1
Release:	1
License:	Python
Group:		Development/Python
Url:		http://labix.org/python-dateutil
Source0:	https://pypi.python.org/packages/54/bb/f1db86504f7a49e1d9b9301531181b00a1c7325dc85a29160ee3eaa73a54/python-dateutil-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools >= 3.0
BuildRequires:	pkgconfig(python3)
Requires:	python >= 3.0

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
python setup.py install --root=%{buildroot}

%files
%doc LICENSE NEWS
%{py_puresitedir}/%{fname}
%{py_puresitedir}/python_%{fname}-%{version}-py%{py_ver}.egg-info

