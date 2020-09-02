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
