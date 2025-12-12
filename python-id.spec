Name:		python-id
Version:	1.5.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/i/id/id-%{version}.tar.gz
Summary:	A tool for generating OIDC identities
URL:		https://pypi.org/project/id/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
A tool for generating OIDC identities

%files
%{py_sitedir}/id
%{py_sitedir}/id-*.*-info
