install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain_gcd

brain_prime:
	poetry run brain_prime

brain_progression:
	poetry run brain_progression

build:
	poetry build

lint:
	poetry run flake8 brain_games
	poetry run flake8 brain-even
	poetry run flake8 brain-calc
	poetry run flake8 brain_gcd
	poetry run flake8 brain_progression
	poetry run flake8 brain_prime



