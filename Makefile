install:
    pip install --upgrade pip &&\
    pip install -r pre-reqs.txt &&\
    pip install pytest-cov &&\
    pip install -r requirements.txt
lint:
    pylint --disable=R,C main.py
test:
    python -m pytest -vv --cov=main test_main.py
run:
    python main.py