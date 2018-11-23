# % global git_hash git10597f7

Name:           openstack-java-sdk
Version:        3.2.5
Release:        1%{?git_hash}%{?dist}
Summary:        OpenStack Java SDK

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/woorea/%{name}
Source0:        https://github.com/woorea/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  java-devel >= 1:1.7.0
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  maven-local
BuildRequires:  jboss-annotations-1.1-api
BuildRequires:  maven-gpg-plugin
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  sonatype-oss-parent
BuildRequires:  mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires:  mvn(org.jboss.resteasy:resteasy-jaxrs)

%description
OpenStack client implementation in Java.


%package -n openstack-java-javadoc
Summary:        Java docs for OpenStack Java SDK
Group:          Documentation

%description -n openstack-java-javadoc
This package contains the API documentation for the OpenStack Java SDK.


%package -n openstack-java-client
Summary:        OpenStack Java Client

%description -n openstack-java-client
This package contains the %{summary}.


%package -n openstack-java-resteasy-connector
Summary:        OpenStack Java RESTEasy Connector

%description -n openstack-java-resteasy-connector
This package contains the %{summary}.


%package -n openstack-java-ceilometer-client
Summary:        OpenStack Java Ceilometer Client

%description -n openstack-java-ceilometer-client
This package contains the %{summary}.


%package -n openstack-java-ceilometer-model
Summary:        OpenStack Java Ceilometer Model

%description -n openstack-java-ceilometer-model
This package contains the %{summary}.


%package -n openstack-java-glance-client
Summary:        OpenStack Java Glance Client

%description -n openstack-java-glance-client
This package contains the %{summary}.


%package -n openstack-java-glance-model
Summary:        OpenStack Java Glance Model

%description -n openstack-java-glance-model
This package contains the %{summary}.


%package -n openstack-java-cinder-client
Summary:        OpenStack Java Cinder Client

%description -n openstack-java-cinder-client
This package contains the %{summary}.


%package -n openstack-java-cinder-model
Summary:        OpenStack Java Cinder Model

%description -n openstack-java-cinder-model
This package contains the %{summary}.


%package -n openstack-java-keystone-client
Summary:        OpenStack Java Keystone Client

%description -n openstack-java-keystone-client
This package contains the %{summary}.


%package -n openstack-java-keystone-model
Summary:        OpenStack Java Keystone Model

%description -n openstack-java-keystone-model
This package contains the %{summary}.


%package -n openstack-java-nova-client
Summary:        OpenStack Java Nova Client

%description -n openstack-java-nova-client
This package contains the %{summary}.


%package -n openstack-java-nova-model
Summary:        OpenStack Java Nova Model

%description -n openstack-java-nova-model
This package contains the %{summary}.


%package -n openstack-java-quantum-client
Summary:        OpenStack Java Quantum Client

%description -n openstack-java-quantum-client
This package contains the %{summary}.


%package -n openstack-java-quantum-model
Summary:        OpenStack Java Quantum Model

%description -n openstack-java-quantum-model
This package contains the %{summary}.


%package -n openstack-java-swift-client
Summary:        OpenStack Java Swift Client

%description -n openstack-java-swift-client
This package contains the %{summary}.


%package -n openstack-java-swift-model
Summary:        OpenStack Java Swift Model

%description -n openstack-java-swift-model
This package contains the %{summary}.


%package -n openstack-java-heat-client
Summary:        OpenStack Java Heat Client

%description -n openstack-java-heat-client
This package contains the %{summary}.


%package -n openstack-java-heat-model
Summary:        OpenStack Java Heat Model

%description -n openstack-java-heat-model
This package contains the %{summary}.


%prep
%setup -q -n %{name}-%{name}-%{version}
%mvn_package ":{openstack-java-sdk,openstack-client-connectors}" __noinstall


%build
%mvn_build -s -- -P "!console,!examples,!jersey2,resteasy" -DskipTests -Dskip.sign=true


%install
%mvn_install


%files -n openstack-java-javadoc -f .mfiles-javadoc
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-client -f .mfiles-openstack-client
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-resteasy-connector -f .mfiles-resteasy-connector
%doc LICENSE.txt README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-ceilometer-client -f .mfiles-ceilometer-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-ceilometer-model -f .mfiles-ceilometer-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-glance-client -f .mfiles-glance-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-glance-model -f .mfiles-glance-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-cinder-client -f .mfiles-cinder-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-cinder-model -f .mfiles-cinder-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-keystone-client -f .mfiles-keystone-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-keystone-model -f .mfiles-keystone-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-nova-client -f .mfiles-nova-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-nova-model -f .mfiles-nova-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-quantum-client -f .mfiles-quantum-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-quantum-model -f .mfiles-quantum-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-swift-client -f .mfiles-swift-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-swift-model -f .mfiles-swift-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-heat-client -f .mfiles-heat-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-heat-model -f .mfiles-heat-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%changelog
* Thu Nov 22 2018 Dominik Holler <dholler@redhat.com> - 3.2.5-1
- update to openstack-java-sdk-3.2.5

* Tue Aug 14 2018 Dominik Holler <dholler@redhat.com> - 3.2.4-1
- update to openstack-java-sdk-3.2.4

* Mon Jul 23 2018 Dominik Holler <dholler@redhat.com> - 3.2.3-1
- update to openstack-java-sdk-3.2.3

* Tue Jun 12 2018 Sandro Bonazzola <sbonazzo@redhat.com> - 3.1.3-2
- Changed build requirements allowing to build on EL7
- Fixed rpmlint issues
- Resolves: BZ#1590327

* Fri Jun 08 2018 Dominik Holler <dholler@redhat.com> - 3.1.3-1
- update to openstack-java-sdk-3.1.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Dominik Holler <dholler@redhat.com> - 3.1.2-1
- update to openstack-java-sdk-3.1.2
- add build-time dependency sonatype-oss-parent

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar  8 2015 Federico Simoncelli <fsimonce@redhat.com> - 3.1.1-1
- update to openstack-java-sdk-3.1.1

* Wed Jan 14 2015 Federico Simoncelli <fsimonce@redhat.com> - 3.0.6-1
- update to openstack-java-sdk-3.0.6

* Fri Jun 27 2014 Federico Simoncelli <fsimonce@redhat.com> - 3.0.5-1
- update to openstack-java-sdk-3.0.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Federico Simoncelli <fsimonce@redhat.com> - 3.0.4-1
- update to openstack-java-sdk-3.0.4

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.0.2-2
- Use Requires: java-headless rebuild (#1067528)

* Tue Jan  7 2014 Federico Simoncelli <fsimonce@redhat.com> - 3.0.2-1
- update to openstack-java-sdk-3.0.2

* Fri Oct  4 2013 Federico Simoncelli <fsimonce@redhat.com> - 3.0.1-1
- update to openstack-java-sdk-3.0.1

* Thu Aug 29 2013 Federico Simoncelli <fsimonce@redhat.com> - 3.0.0-2
- resteasy: add support for resteasy 3

* Wed Aug 28 2013 Federico Simoncelli <fsimonce@redhat.com> - 3.0.0-1
- update to openstack-java-sdk-3.0.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-0.1.git10597f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Federico Simoncelli <fsimonce@redhat.com> - 3.0.0-0.0.git10597f7
- Initial build
