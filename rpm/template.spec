Name:           ros-kinetic-roscpp-core
Version:        0.6.2
Release:        0%{?dist}
Summary:        ROS roscpp_core package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/roscpp_core
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-cpp-common
Requires:       ros-kinetic-roscpp-serialization
Requires:       ros-kinetic-roscpp-traits
Requires:       ros-kinetic-rostime
BuildRequires:  ros-kinetic-catkin

%description
Underlying data libraries for roscpp messages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Feb 14 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.2-0
- Autogenerated by Bloom

* Fri Sep 02 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.1-0
- Autogenerated by Bloom

* Thu Mar 17 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.0-0
- Autogenerated by Bloom

* Wed Mar 09 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.7-0
- Autogenerated by Bloom

