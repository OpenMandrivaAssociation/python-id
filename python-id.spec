%define module id

Name:		python-id
Version:	1.6.1
Release:	1
Summary:	A tool for generating OIDC identities
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/id/
Source0:	https://files.pythonhosted.org/packages/source/i/id/id-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
A tool for generating OIDC identities

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
