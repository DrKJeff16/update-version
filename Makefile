.PHONY: all help lint build local-install clean docs vim-eof-comment update distclean

all: distclean
	@$(MAKE) local-install

update:
	@pipenv lock
	@pipenv sync
	@pipenv sync --dev
	@pipenv clean

clean:
	@echo "Cleaning..."
	@rm -rf build dist *.egg-info
	@echo -e "Done!"

distclean: clean
	@echo "Cleaning Everything..."
	@rm -rf .mypy_cache .ropeproject .pytest_cache .ruff_cache
	@echo -e "Done!"

docs:
	@echo -e "Generating docs..."
	@$(MAKE) -C docs html
	@echo -e "Done!"

help:
	@echo -e "Available targets:\n"
	@echo "  build"
	@echo "  clean"
	@echo "  distclean"
	@echo "  docs"
	@echo "  help"
	@echo "  lint"
	@echo "  local-install"
	@echo "  stubs"
	@echo

lint:
	@echo "Linting..."
	@pipenv run flake8 --statistics --show-source --color=always --max-line-length=100 --ignore=D401 \
		--per-file-ignores=__init__.py:F401 \
		--exclude .tox,.git,*staticfiles*,build,locale,docs,tools,venv,.venv,*migrations*,*.pyc,*.pyi,__pycache__,test_*.py \
		update_version
	@pipenv run pydocstyle --convention=numpy --match='.*\.py' update_version
	# @pipenv run autopep8 --aggressive --aggressive --aggressive --in-place --recursive update_version
	$(eval files := $(shell fd --full-path update_version -e py))
	@pipenv run numpydoc lint $(files)
	@echo "Done!"

stubs: lint
	@echo "Generating stubs..."
	@pipenv run stubgen --include-docstrings --include-private -v -p update_version -o .
	@echo -e "Done!\nRunning isort..."
	@pipenv run isort update_version
	@echo -e "Done!\nLinting with mypy..."
	@pipenv run mypy update_version
	@echo "Done!"

format: stubs ## Format using Ruff
	@echo "Formatting with Ruff..."
	@pipenv run ruff format update_version
	@echo -e "Done!\n\nChecking with Ruff..."
	@pipenv run ruff check update_version
	@echo "Done!\nRunning vim-eof-comment..."
	@pipenv run vim-eof-comment -e py,pyi,md,Makefile,yaml,yml,toml -nv .
	@echo "Done!"

build: format
	@echo -e "Building..."
	@pipenv run python3 -m build
	@echo -e "Done!"

local-install: build
	@echo -e "Installing locally..."
	@pipenv run python3 -m pip install .
	@echo -e "Done!"

# vim: set ts=4 sts=4 sw=0 noet ai si sta:
