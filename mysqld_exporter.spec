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

%files
%{_bindir}/%{name}


%changelog
* Mon May 13 2024 Ivan Ivanov <kasper_wps@mail.ru>
- First release
