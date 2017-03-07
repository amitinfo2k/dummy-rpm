Name: sxp-dummy
Version:  %{version}
Release:  %{release}%{?dist}
Summary:  dummy rpm packg

License:  GPL
URL:   None
Source:  sxp-dummy.tar

%description
dummy rpm image

%prep
%setup -n sxp-dummy

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt
cp -R * $RPM_BUILD_ROOT/opt

%files
/opt

%clean
rm -rf $RPM_BUILD_ROOT
