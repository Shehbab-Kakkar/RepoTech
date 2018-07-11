Name:           Round-the-Clock
Version:        0.1
Release:        31
Summary:         Round the Clock

License:        GvL2
URL:            https://github.com/Shehbab-Kakkar
Source0:        roundtheclock-01.src.tar.gz


%description
Round the Clock

%prep
%setup -n roundtheclock

%install
mkdir -p "$RPM_BUILD_ROOT"
cp -R * "$RPM_BUILD_ROOT"
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/etc/yum.repos.d/repo/
%exclude /etc/yum.repos.d/repo/.git/
