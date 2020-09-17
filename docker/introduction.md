

```
sudo systemctl start docker
#show exsiting images
sudo docker images
#display only image-id
sudo docker images --quiet
#remove all
sudo docker rmi $(sudo docker images --quiet)


#show exsiting container
sudo docker container ls -a

sudo docker container rm {container_id}


##stop
sudo docker contanier stop {container_name}
```
