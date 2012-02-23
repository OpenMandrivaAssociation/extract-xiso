Name:		extract-xiso
Version:	2.5
Release:	%mkrel 1
Summary:	A backup tool for creating and extracting disc image .iso's of XBox games
License:	BSD
Group:		Archiving/Backup
URL:		http://sourceforge.net/projects/extract-xiso
Source0:	%{name}_v%{version}_src.tgz

%description
A backup tool for creating and extracting disc image .iso's of XBox games.
For more details see: http://sourceforge.net/projects/extract-xiso

%prep
%setup -q -n %{name}

%build
%setup_compile_flags
gcc -D__LINUX__ $CFLAGS $LDFLAGS extract-xiso.c libftp-*/*.c -o extract-xiso

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__cp %{name} %{buildroot}%{_bindir}/

%clean
%__rm -rf %{buildroot}

%files
%doc LICENSE.TXT README.TXT
%{_bindir}/%{name}

