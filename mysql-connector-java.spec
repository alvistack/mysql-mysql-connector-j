# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

%global __strip /bin/true

%global __brp_mangle_shebangs /bin/true

Name: mysql-connector-java
Epoch: 100
Version: 8.2.0
Release: 1%{?dist}
BuildArch: noarch
Summary: MySQL Connector/J
License: GPL-2.0-or-later
URL: https://github.com/mysql/mysql-connector-j/tags
Source0: %{name}_%{version}.orig.tar.gz
Requires: java

%description
MySQL provides connectivity for client applications developed in the
Java programming language with MySQL Connector/J, a driver that
implements the Java Database Connectivity (JDBC) API and also MySQL X
DevAPI.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%install
install -Dpm755 -d %{buildroot}%{_datadir}/java
install -Dpm755 -t %{buildroot}%{_datadir}/java mysql-connector-j-*.jar
pushd %{buildroot}%{_datadir}/java && \
    ln -fs mysql-connector-j-*.jar mysql-connector-j.jar && \
    ln -fs mysql-connector-j.jar mysql-connector-java.jar && \
    popd

%check

%files
%license LICENSE
%dir %{_datadir}/java
%{_datadir}/java/*

%changelog
