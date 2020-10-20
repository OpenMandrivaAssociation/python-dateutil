%define fname dateutil

Summary:	Provides powerful extensions to the standard datetime module
Name:		python-dateutil
Version:	2.8.1
Release:	2
License:	Python
Group:		Development/Python
Url:		https://dateutil.readthedocs.io/en/stable/
# https://pypi.org/project/python-dateutil
Source0:	https://pypi.python.org/packages/source/p/python-dateutil/python-%{fname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools >= 3.0
BuildRequires:	python3dist(setuptools-scm)
BuildRequires:	pkgconfig(python3)
Requires:	python >= 3.0
Requires:	timezone

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
%autosetup -p1
rm -rf python_dateutil.egg-info/

iconv --from=ISO-8859-1 --to=UTF-8 NEWS > NEWS.new
mv NEWS.new NEWS

%build
%py3_build

%install
%py3_install

%files
%doc LICENSE NEWS
%{py_puresitedir}/%{fname}
%{py_puresitedir}/python_%{fname}-%{version}-py%{py_ver}.egg-info
