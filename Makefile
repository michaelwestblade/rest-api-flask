start:
	docker run -p 5005:5000 -w /app -v "$$(pwd):/app" flask-api