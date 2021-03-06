install:
	poetry install

brain-games: 
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

make lint:
	poetry run flake8 brain_games
	poetry run flake8 brain_even
	poetry run flake8 brain_calc
	poetry run flake8 brain-gcd