.PHONY: show-help
## Show help screen
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)";echo;sed -ne"/^## /{h;s/.*//;:d" -e"H;n;s/^## //;td" -e"s/:.*//;G;s/\\n## /---/;s/\\n/ /g;p;}" ${MAKEFILE_LIST}|LC_ALL='C' sort -f|awk -F --- -v n=$$(tput cols) -v i=29 -v a="$$(tput setaf 6)" -v z="$$(tput sgr0)" '{printf"%s%*s%s ",a,-i,$$1,z;m=split($$2,w," ");l=n-i;for(j=1;j<=m;j++){l-=length(w[j])+1;if(l<= 0){l=n-i-length(w[j])-1;printf"\n%*s ",-i," ";}printf"%s ",w[j];}printf"\n";}'

.PHONY: lint
## Run linting and formatting
lint:
	@poetry run ruff check .
	@poetry run ruff format --check .

.PHONY: lint-fix
## Fix linting/formatting issues
lint-fix:
	@poetry run ruff check --fix . || true
	@poetry run ruff format .
	@poetry run ruff check .

.PHONY: typecheck
## Run type checks for python
typecheck:
	@poetry run pyright

.PHONY: deptry
## Check for unused dependencies
deptry:
	@poetry run deptry .

.PHONY: vulture
## Check for unused code
vulture:
	@poetry run vulture .

.PHONY: test
## Run unit tests
test:
	@poetry run python -m pytest