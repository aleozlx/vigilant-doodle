#!/bin/bash

if [[ $1 == rebuild ]]; then
  docker build -t aleozlx/vigilant-doodle .
  docker push aleozlx/vigilant-doodle
fi

kubectl scale --replicas 0 replicationcontroller/celery-repctl && kubectl scale --replicas 1 replicationcontroller/celery-repctl
kubectl port-forward --address 0.0.0.0 service/celery-gateway 8888:80

