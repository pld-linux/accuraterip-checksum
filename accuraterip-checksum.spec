Summary:	A C99 commandline program to compute the AccurateRip checksum
Name:		accuraterip-checksum
Version:	1.5
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/leo-bogert/accuraterip-checksum/archive/version%{version}.tar.gz
# Source0-md5:	e189ef0a849923facb46ef82d22c1f4d
URL:		https://github.com/leo-bogert/accuraterip-checksum
BuildRequires:	libsndfile-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C99 commandline program to compute the AccurateRip checksum of
singletrack WAV files. Implemented according to
http://www.hydrogenaudio.org/forums/index.php?showtopic=97603

%prep
%setup -q -n %{name}-version%{version}

%build
%{__cc} %{rpmcflags} accuraterip-checksum.c -o %{name} %{rpmldflags} -lsndfile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
cp -p %{name} $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
