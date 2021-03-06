# PrestaShop
------
**This is NOT meant for production purposes!!**
This should work with all OS as long as you have Docker and Docker Compose installed.  Please report any issues you face and I'll take a look as soon as I can.

-------

### What does it do?
Generates a Docker container with any version of PrestaShop. This helps anyone testing an extension or just wanting to play around with a test PrestaShop site.

### How do I monitor the app created?
I personally use Docker Desktop but you can use Portainer or any other docker monitoring system you want!

### Start PrestaShop
Select the version from the dropdown and click on the "up" button below to create the app. 

You then want to run the command below in your terminal to get the PrestaShop container id
```
docker container ls
``` 
Find the one that says "bitnami/prestashop:1.x" and use that container id in place of <container-id> in the command below.

Install SSH and run it
```
docker exec -it <container-id> bash -c "apt-get update; apt-get install -y openssh-server; mkdir -p /var/run/sshd; echo 'root:root' |chpasswd; sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config; sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config; mkdir -p /root/.ssh; sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd; echo -e "root\nroot" | passwd; service ssh restart;"
```


**You will need to run the below command each time you start the container to enable ssh**
```
docker exec <container-id> service ssh restart
```

### Useful info
**PrestaShop Admin Panel:** localhost/admin

**PrestaShop Admin User:** user@example.com

**PrestaShop Admin Pass:** bitnami1

**SSH Admin User:** root

**SSH Admin Pass:** root