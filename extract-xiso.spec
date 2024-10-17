Name:		extract-xiso
Version:	2.7.1
Release:	2
Summary:	A backup tool for creating and extracting disc image .iso's of XBox games
License:	BSD
Group:		Archiving/Backup
URL:		https://sourceforge.net/projects/extract-xiso
Source0:	%{name}-%{version}.tar.gz

%description
A backup tool for creating and extracting disc image .iso's of XBox games.
For more details see: http://sourceforge.net/projects/extract-xiso

%prep
%setup -q -n %{name}

%build
%setup_compile_flags
gcc -D__LINUX__ $CFLAGS $LDFLAGS extract-xiso.c libftp-*/*.c -o extract-xiso

%install
mkdir -p %{buildroot}%{_bindir}
cp %{name} %{buildroot}%{_bindir}/

%files
%doc LICENSE.TXT README.TXT
%{_bindir}/%{name}

