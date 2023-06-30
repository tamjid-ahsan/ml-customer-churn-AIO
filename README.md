# docker-nginx-uwsgi-flask README
WIP
ML application deployment using `Docker` <img src="https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/Docker_logo.svg/120px-Docker_logo.svg.png" alt="Docker" height="5%" width="5%">. `Flask` [<img src= "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/120px-Flask_logo.svg.png" alt="Flasklogo" height="5%" width="5%" title="Flask">](https://github.com/pallets/flask) as API server, `NGINX` [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Nginx_logo.svg/120px-Nginx_logo.svg.png" alt="NGINX" height="5%" width="5%">](https://hg.nginx.org/nginx) and `uWSGI` [<img src="https://www.fullstackpython.com/img/logos/uwsgi.png" alt="uWSGI" height="5%" width="5%">](https://github.com/unbit/uwsgi) for request management.
ML details is [available at](https://github.com/tamjid-ahsan/capstone_customer_churn).

___ 
### useful commands

```bash
# while in the directory, cd into the folder containing yml file
docker-compose build # build containers
docker-compose up -d # run containers in detached mode 
docker-compose up --build # rebuild 
docker-compose images # all images built
docker-compose ps # show running processes

# Stop services only
docker-compose stop

# Stop and remove containers, networks..
docker-compose down 

# Down and remove volumes
docker-compose down --volumes 

# Down and remove images
docker-compose down --rmi <all|local> 

sudo ss -tulpn | grep LISTEN # list all used ports and process associated
sudo killall apache2 # kill a process if it using a port
```
- peek into images | containers
    - [dive](https://github.com/wagoodman/dive)
    - [podman](https://podman.io/)

## References
- [command](https://www.cyberciti.biz/faq/unix-linux-check-if-port-is-in-use-command/)
- [create-a-multipage-dash-app](https://medium.com/@mcmanus_data_works/how-to-create-a-multipage-dash-app-261a8699ac3f)
- https://www.digitalocean.com/community/tutorials/how-to-set-up-uwsgi-and-nginx-to-serve-python-apps-on-ubuntu-14-04
- https://theaisummer.com/uwsgi-nginx/
- https://docs.nginx.com/nginx/admin-guide/web-server/app-gateway-uwsgi-django/
- https://www.enterprisedb.com/blog/reverse-proxying-pgadmin-uwsgi-and-nginx
- https://www.shubhamdipt.com/blog/nginx-configuration-set-up-with-uwsgi/
- https://uwsgi-docs.readthedocs.io/en/latest/Nginx.html
- https://gabimelo.medium.com/developing-a-flask-api-in-a-docker-container-with-uwsgi-and-nginx-e089e43ed90e
- https://www.youtube.com/watch?v=wLrmmh1eI94
https://www.youtube.com/watch?v=7VAI73roXaY
https://www.youtube.com/watch?v=cjJVmAI1Do4
https://www.youtube.com/watch?v=ZmH1L1QeNHk
https://www.youtube.com/watch?v=iaQBEwc9HRg
https://www.youtube.com/watch?v=mZbLvGQqEvY
https://www.youtube.com/watch?v=2ImyICAC8nA
https://www.youtube.com/results?search_query=nginx+uwsgi+docker-compose
https://www.youtube.com/watch?v=dVEjSmKFUVI
https://www.youtube.com/watch?v=NIHzYIkXFhE
https://www.youtube.com/watch?v=42Q65H8ch7U
https://www.youtube.com/watch?v=ugRoOFYJyJ8
https://devpress.csdn.net/cloudnative/62f220b7c6770329307f6048.html
https://www.bogotobogo.com/DevOps/Docker/Docker-Compose-Nginx-Reverse-Proxy-Multiple-Containers.php
https://stackoverflow.com/questions/61094884/how-to-run-2-flask-apps-and-nginx-using-a-single-docker-compose
https://devpress.csdn.net/cloudnative/62f220b7c6770329307f6048.html



___
contact: <a href="mailto:tamz888@yahoo.com">tamz888@yahoo.com</a> [<img src="./flask/app/data/TAlogo1.png" alt="TA" height="3%" width="3%">](http://linkedin.com/in/tamjidahsan/)
___

## TODO:

- <s>***fix app to app api calls inside docker container***</s>
- change default favicon for apps
- create a new image from multiple dockerfile and docker-compose to a single image {check if is it is possible?}
- deep dive into docker and docker-compose
- secure connection: SSL, port 443 in nginx and certificate
- add architecture diagram
- adding custom package to the run.py or wherever needed. package importing deep dive | folder traversing | __init__ explore
- run jupyter server in app 

# instructions

- TBA