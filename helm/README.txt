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
