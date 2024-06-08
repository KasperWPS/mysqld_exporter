Name:           mysqld_exporter
Version:        %{version_}
Release:        %{release_}%{?dist}
Summary:        MySQL exporter v.%{version}

License:        GPLv2.1
#URL:            
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang
Requires:       mariadb-server >= 10.11

Provides:       %{name} = %{version}

%description
Prometheus exporter for MySQL server metrics.

%global debug_package %{nil}

%prep
%autosetup


%build
make build

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 dep/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 dep/%{name} %{buildroot}%{_sysconfdir}/default/%{name}

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/default/%{name}

%changelog
* Mon May 13 2024 Ivan Ivanov <kasper_wps@mail.ru>
- First release
* Sat Jun 08 2024 Ivan Ivanov <kasper_wps@mail.ru>
- bugfix built.sh
- add service file and config