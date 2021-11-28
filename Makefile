dev:
	pip3 install -U pip pipenv
	pipenv install --dev

watch:
	sam sync --stack-name s3-app --watch
