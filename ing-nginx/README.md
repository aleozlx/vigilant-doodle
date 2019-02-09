kubectl create -f rbac-config.yaml
helm init --upgrade --service-account tiller
helm install --name nginx --set rbac.create=true stable/nginx-ingress
kubectl create -f celery-ingress.yml

**Reverse Proxy:** router -> ingress
```nginx
    upstream nginxIngress {
        server 192.168.20.30;
        server 192.168.20.31;
    }

    server {
	    listen 80;
	    server_name hotwings.3cv-research.com;
	    location / {
	        proxy_pass http://nginxIngress;
            proxy_set_header Host            $host;
	        proxy_set_header X-Forwarded-For $remote_addr;
        }
    }
```

OR **Without Ingress**

```
kubectl port-forward --address 0.0.0.0 service/celery-runner 5000:80
```
```nginx
    server {
	    listen 80;
	    server_name hotwings.3cv-research.com;
	    location / {
	        proxy_pass http://localhost:5000;
        }
    }
```

