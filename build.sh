#!/bin/bash

set -e

VERSION='0.0.0'
RELEASE='0'

rm -rf ~/rpmbuild

export GOPATH=~/go
export PATH=${PATH}:${GOPATH}/bin

mkdir -p ${GOPATH}/{bin,pkg,src}

sudo dnf install git make golang rpmdevtools -y

if [ ! -d mysqld_exporter ]; then
  git clone https://github.com/prometheus/mysqld_exporter
fi

cd mysqld_exporter
git pull
VERSION=$(git describe | grep -o '[0-9]\{0,\}\.[0-9]\{1,\}.[0-9]\{1,\}')
RELEASE=$(git describe | grep -o '\-[0-9]\{1,\}\-' | grep -o '[0-9]\{1,\}')

rpmdev-setuptree

# Download project dependencies
go mod tidy
cd ..

mkdir -p mysqld_exporter/dep
cp dep/mysqld_exporter mysqld_exporter/dep
cp dep/mysqld_exporter.service mysqld_exporter/dep

tar czf mysqld_exporter-${VERSION}.tar.gz mysqld_exporter --transform s/mysqld_exporter/mysqld_exporter-${VERSION}/

mv mysqld_exporter-${VERSION}.tar.gz ~/rpmbuild/SOURCES

rpmbuild -ba --define "version_ ${VERSION}" --define "release_ ${RELEASE}" mysqld_exporter.spec
