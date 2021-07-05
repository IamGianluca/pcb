test: 
	pytest -vv -s  &&\
	mypy .

format:
	isort . && \
	black -l 79 .