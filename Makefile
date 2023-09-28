image-name = anon-discourse-image
instance-name = anon-discourse

clean:
	docker rm $(instance-name)

build:
	docker build -t $(image-name) ./

run: clean build
	docker run --name $(instance-name) -p 5000:5000 $(image-name)

run-local:
	python3 ./src/main.py