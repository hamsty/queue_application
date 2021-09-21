FROM centos:7
EXPOSE 5678/tcp
RUN rpmkeys --import file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 && \
    yum -y update && \
    yum clean all
RUN yum install -y python3 pip3
ADD /Queue_Application /modules/Queue_Application/
ADD /Queue_Application/config /etc/Queue_Application/config/
WORKDIR /modules/Queue_Application
RUN python3 setup.py install
WORKDIR /root
RUN rm -d -r /modules