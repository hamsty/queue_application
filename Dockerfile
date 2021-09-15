FROM centos:7
EXPOSE 5678/tcp
RUN rpmkeys --import file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 && \
    yum -y update && \
    yum clean all
RUN yum install -y python3 pip3
RUN pip3 install twisted
ADD ./qapp/ /modules/qapp/
ENV PYTHONPATH=/modules
WORKDIR /modules/qapp