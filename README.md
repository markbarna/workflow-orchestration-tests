# workflow-orchestration-tests

## Registry notes
```
Add registry to: `/etc/hosts`
`127.0.0.1 k3d-argo-2`

# You can now use the registry like this (example):
# 1. create a new cluster that uses this registry
k3d cluster create --registry-use k3d-argo-2:59217

# 2. tag an existing local image to be pushed to the registry
docker tag nginx:latest k3d-argo-2:59217/mynginx:v0.1

# 3. push that image to the registry
docker push k3d-argo-2:59217/mynginx:v0.1

# 4. run a pod that uses this image
kubectl run mynginx --image k3d-argo-2:59217/mynginx:v0.1
```