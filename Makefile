dev:
	pip3 install -U pip pipenv
	pipenv install --dev

watch:
	sam sync --stack-name s3-app --watch

clean:
	rm -Rf .mypy_cache
	rm -Rf .pytest_cache tests/.pytest_cache
	rm -Rf .idea
	rm -Rf .aws-sam
	pipenv --rm || true
