## install
sudo yum update -y  
sudo yum install docker  
sudo systemctl start docker  

## example
sudo docker container run hello-world  
#-d represents running coutainer in background  
sudo docker container run -d --name hoge1 --p 8080:80 httpd  
#remove  
sudo docker container rm hoge1  
#if you wanto see logs 
sudo docker container logs hoge1 -f

#create volume  
sudo docker volume create --name mysqlvolume



## network  
sudo docker network ls
sudo docker container run  -name hoge -p 8080:80 httpd  
sudo docker cointaner inspect hoge

sudo docker network create my-network  
sudo docker network inspect my-network  
sudo docker container run --name hoge -d -p 8080:80 --net my-network httpd  
sudo docker network inspect my-network
