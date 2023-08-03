install:
	pip install --upgrade pip
	pip install -r requirements.txt  
lint:
	pylint --disable=R,C main.py
test:
	python -m pytest -v --cov=main test_main.py
run:
	python main.py
