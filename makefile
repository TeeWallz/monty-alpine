# Allow 2 parallel makes
MAKEFLAGS += -j2

hello:
	echo "Hello, World"

watch_http:
	watch-http-server dist/

watch_sass:
	sass --watch assets/scss/main.scss main.css

watch_tailwind:
	npx tailwindcss -i ./src/tailwindcss/main.tailwind.css -o ./dist/assets/css/main.css --watch

watch: watch_http watch_tailwind




