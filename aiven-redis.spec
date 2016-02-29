Name:           aiven-redis
Version:        %{major_version}
Release:        %{minor_version}%{?dist}
Url:            http://github.com/ohmu/pghoard
Summary:        Aiven Redis support package
License:        ASL 2.0
Source0:        aiven-redis-rpm-src.tar.gz
Requires(pre):  shadow-utils

%define debug_package %{nil}

%description
Aiven Redis support package

%prep
%setup -q -n aiven-redis

%build
make

%install
%{__install} -Dm0644 src/redis-sentinel %{buildroot}/opt/aiven-redis/redis-sentinel
%{__mkdir_p} %{buildroot}/opt/aiven-redis
%{__install} -Dm0644 aiven-redis-sentinel.unit %{buildroot}%{_unitdir}/aiven-redis-sentinel.service

%files
%defattr(-,root,root,-)
%{_unitdir}/aiven-redis-sentinel.service
%attr(755, root, root) /opt/aiven-redis/redis-sentinel

%changelog
* Mon Feb 29 2016 Mika Eloranta <mel@aiven.io> - 3.2
- First version
