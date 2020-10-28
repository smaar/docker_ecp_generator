# Magento 2
------
**This is NOT meant for production purposes!!**
This should work with all OS as long as you have docker and docker compose installed.  Please report any issues you face and I'll take a look as soon as I can.

-------

### What does it do?
Generates a docker app with any version of Magento 2. This helps anyone testing an extension or just wanting to play around with a test Magento 2 site.

### How do I monitor the app created?
I personally use docker desktop but you can use portainer or any other docker monitoring system you want!

### Start Magento 2.x
Select the version from the dropdown and click on the "up" button below to create the app.  

You then want to run the command below in your terminal to get the magento container id
`docker container ls` 
Find the one that says "magento2.x.x" and use that container id in place of <container-id> in the command below.

**You will be asked to [authenticate](https://devdocs.magento.com/guides/v2.4/install-gde/prereq/connect-auth.html "authenticate") during this process.**
Please note that you will need to pick the command for your operating system.
`docker exec -it <container-id> bash -c "/opt/bitnami/magento/htdocs/bin/magento deploy:mode:set developer; php -d memory_limit=4G /opt/bitnami/magento/htdocs/bin/magento sampledata:deploy; /opt/bitnami/magento/htdocs/bin/magento setup:upgrade; /opt/bitnami/magento/htdocs/bin/magento setup:di:compile; apt-get update; apt-get install -y openssh-server; mkdir -p /var/run/sshd; echo 'root:root' |chpasswd; sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config; sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config; mkdir -p /root/.ssh; sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd; echo -e "root\nroot" | passwd; service ssh restart;"`


**You will need to run the below command each time you start the container to enable ssh access**
`docker exec <container-id> service ssh restart`

### Useful info
**Magento Admin Panel:** 127.0.0.1/admin

**Magento Admin User:** user

**Magento Admin Pass:** bitnami1

**SSH Admin User:** root

**SSH Admin Pass:** root