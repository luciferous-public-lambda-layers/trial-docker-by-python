import docker

client = docker.from_env()

resp = client.containers.run("hello-world")
print(resp)
