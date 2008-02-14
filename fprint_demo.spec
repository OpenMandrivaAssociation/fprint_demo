Name: fprint_demo
Version: 0.4
Release: %mkrel 1
Summary: Simple GTK+ application to demonstrate and test libfprint's capabilities
License: GPL
Source: http://prdownloads.sourceforge.net/fprint/fprint_demo-0.4.tar.bz2
BuildRequires: libfprint-devel
BuildRequires: libgtk+2.0-devel
Group: System/Configuration/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
fprint_demo is a simple GTK+ application to demonstrate and test libfprint's
capabilities. It is written in C and licensed under the GNU GPL v2.

It provides access to many of the features offered by the backing library,
libfprint. 

%prep
%setup -q

%build
%configure
%make

%install
rm -Rf %{buildroot}
%makeinstall_std

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
