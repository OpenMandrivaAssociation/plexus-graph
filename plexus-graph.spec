# TODO: junit QA tests

Name:           plexus-graph
Version:        0.13.1
Release:        7
Summary:        Graph data structures manipulation library

Group:          Development/Java
License:        CPL
URL:            http://plexus.sourceforge.net/
Source0:        http://download.sourceforge.net/plexus/plexus-src-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       log4j apache-commons-collections java jpackage-utils
BuildRequires:  %{requires} ant java-devel

BuildArch:      noarch

%description
Plexus is a Java library with specifications and implementations for
generic graph data structures. Like the Java Collections Framework,
vertices and edges are containers for arbitrary user-defined objects. 


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n plexus-%{version}


%build
CLASSPATH=$(build-classpath commons-collections log4j) ant dist javadoc


%install
rm -rf $RPM_BUILD_ROOT

# Directory structure
install -d $RPM_BUILD_ROOT%{_javadir}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JARs and JavaDoc
install -m 644 build/dist/plexus-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -rp doc/javadoc/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_javadir}/*
%doc CHANGELOG LICENSE README


%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


