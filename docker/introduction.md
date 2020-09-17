

```
sudo systemctl start docker
#show exsiting images
sudo docker images
#display only image-id
sudo docker images --quiet
#remove all
sudo docker rmi $(sudo docker images --quiet)

```
