# docker build -t jenfi-webserver:latest .
# docker rmi -f jenfi-webserver:latest
# docker rm jenfi-cnt ; docker run --name jenfi-cnt -it --mount "type=bind,source=$(pwd)/,target=/code/" -p 8000:8080 jenfi-webserver:latest
# or
# docker start -a jenfi-cnt
# CMD ["python", "manage.py", "runserver"]
#
# learnings
# install `uwsgi` in image, requirement.txt also download `uwsgi-plugin-python3`
# module in uwsgi config.wsgi
# plugin python3
#
# attach docker to minikube
# eval $(minikube docker-env)
# helm install jenfi install
# helm lint helm
# helm install --debug --dry-run jenfi helm
# helm install --debug --dry-run jenfi-webserver helm/ -f webserver.yaml
# helm install --debug --dry-run jenfi-worker helm/ -f worker.yaml

# helm file doc
# https://helmfile.readthedocs.io/en/latest/#values-files-templates

# install helm diff [required for apply]
# helm plugin install https://github.com/databus23/helm-diff

#    - vars/vars.yaml.gotmpl
#    - vars/secrets.yaml.gotmpl
#    - vars/{{ requiredEnv "ENVIRONMENT" }}/vars.yaml.gotmpl
#    - vars/{{ requiredEnv "ENVIRONMENT" }}/secrets.yaml.gotmpl
#    - vars/{{ requiredEnv "ENVIRONMENT" }}/{{ requiredEnv "REGION" }}/vars.yaml.gotmpl
#    - vars/{{ requiredEnv "ENVIRONMENT" }}/{{ requiredEnv "REGION" }}/secrets.yaml.gotmpl
#    - vars/{{ $service }}-vars.yaml.gotmpl
#    - vars/{{ $service }}-secrets.yaml.gotmpl
#    - vars/{{ requiredEnv "ENVIRONMENT" }}/{{ $service }}-vars.yaml.gotmpl
#    - vars/{{ requiredEnv "ENVIRONMENT" }}/{{ $service }}-secrets.yaml.gotmpl
#    - vars/{{ requiredEnv "ENVIRONMENT" }}/{{ requiredEnv "REGION" }}/{{ $service }}-vars.yaml.gotmpl
#    - vars/{{ requiredEnv "ENVIRONMENT" }}/{{ requiredEnv "REGION" }}/{{ $service }}-secrets.yaml.gotmpl


# set environment varibale for namespace
# helmfile
# lint
# helmfile lint --environment local

# diff
# helmfile diff --environment local

# apply
# helmfile apply --environment local

# cluster autoscaler - example auto discovery
# nginx controller

# aws load balancer

# anton putra youtube
# https://antonputra.com/

# eksctl to create kubernetes
# gpg with git crypt