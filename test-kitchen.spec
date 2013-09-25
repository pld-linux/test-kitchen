#
# Conditional build:
%bcond_with	tests		# build without tests

%define		rel		1
%define		subver	beta.3
Summary:	A Chef convergence integration test harness
Name:		test-kitchen
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.%{subver}.gem
# Source0-md5:	f93168613f72fcca512a0e23d546461f
URL:		https://github.com/opscode/test-kitchen
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-aruba < 1
BuildRequires:	ruby-aruba >= 0.5
BuildRequires:	ruby-bundler < 2
BuildRequires:	ruby-bundler >= 1.3
BuildRequires:	ruby-cane
BuildRequires:	ruby-countloc
BuildRequires:	ruby-fakefs
BuildRequires:	ruby-guard-cucumber
BuildRequires:	ruby-guard-minitest
BuildRequires:	ruby-maruku
BuildRequires:	ruby-minitest < 5
BuildRequires:	ruby-minitest >= 4.7
BuildRequires:	ruby-mocha
BuildRequires:	ruby-rake
BuildRequires:	ruby-simplecov
BuildRequires:	ruby-tailor
BuildRequires:	ruby-yard
%endif
Requires:	ruby-celluloid
Requires:	ruby-mixlib-shellout
Requires:	ruby-net-scp
Requires:	ruby-net-ssh
Requires:	ruby-pry
Requires:	ruby-rubygems > 1.3.1
Requires:	ruby-safe_yaml < 0.10
Requires:	ruby-safe_yaml >= 0.9.5
Requires:	ruby-thor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Chef convergence integration test harness.

%prep
%setup -q
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md LICENSE
%attr(755,root,root) %{_bindir}/kitchen
%{ruby_vendorlibdir}/kitchen.rb
%{ruby_vendorlibdir}/kitchen
# FIXME should be in subdir of this package, or unvendored
%dir %{ruby_vendorlibdir}/vendor
%{ruby_vendorlibdir}/vendor/hash_recursive_merge.rb
