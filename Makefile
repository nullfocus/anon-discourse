image-name = anon-discourse-image
instance-name = anon-discourse

clean:
	- docker rm $(instance-name)

build:
	docker build -t $(image-name) ./

run: clean build
	docker run --name $(instance-name) -p 5000:5000 $(image-name)

run-local:
	python3 ./src/main.py

test: build
	docker run \
		--rm \
		-v ./tests:/usr/src/app/tests \
		--workdir /usr/src/app/tests \
		--entrypoint pytest \
		$(image-name) \
		.

lint:
	docker run \
		--rm \
		-v ./src:/usr/src/app \
		--workdir /usr/src/app \
		pyfound/black:latest_release \
		black \
		.
