# Makefile

VENV_NAME := env
MKDIR_P := mkdir -p
RM_RF := rm -rf
PYTHON := python3

# Detect the operating system
ifeq ($(OS),Windows_NT)
	VENV_ACTIVATE := .\$(VENV_NAME)\Scripts\activate.bat
	RM_RF := del /s /q
	MKDIR_P := mkdir
	GREEN_COLOR := ""
	NC := ""
else
	VENV_ACTIVATE := . ./$(VENV_NAME)/bin/activate
	GREEN_COLOR := \033[0;32m
	NC := \033[0m
endif

# Create Python3 virtual environment and setup project
setup:

	@echo "$(GREEN_COLOR)===Installing pipenv===$(NC)"
	@pip3 install pipenv; \
	pipenv install;

	@echo "$(GREEN_COLOR)=== Installing pre-commit ===$(NC)"
	@pipenv run pip install pre-commit
	@pipenv run pre-commit install

	@# Create .env file with content
	@if [ ! -f .env ]; then \
		echo "$(GREEN_COLOR).env file not found. Generating one...$(NC)"; \
		echo "# Secret key for Django project" > .env; \
		echo "SECRET_KEY = <YOUR_SECRET_KEY>" >> .env; \
		echo "" >> .env; \
		echo "# Database Credentials Changes for .env" >> .env; \
		echo "DB_NAME = <YOUR_DB_NAME>" >> .env; \
		echo "DB_USER = <YOUR_DB_USER>" >> .env; \
		echo "DB_PASSWORD = <YOUR_DB_PASSWORD>" >> .env; \
		echo "DB_HOST = <YOUR_DB_HOST>" >> .env; \
		echo "DB_PORT = <YOUR_DB_PORT>" >> .env; \
		echo "" >> .env; \
		echo "# Google cloud login api" >> .env; \
		echo "GOOGLE_OAUTH2_CLIENT_ID = <YOUR_GOOGLE_OAUTH2_CLIENT_ID>" >> .env; \
		echo "GOOGLE_OAUTH2_SECRET_KEY = <YOUR_GOOGLE_OAUTH2_SECRET_KEY>" >> .env; \
		echo "GOOGLE_OAUTH2_CALLBACK_URL = <YOUR_GOOGLE_OATUH2_CALLBACK_URL>" >> .env; \
	else \
		echo "$(GREEN_COLOR).env file already exists. Skipping creation.$(NC)"; \
	fi
	@echo "$(GREEN_COLOR)Setup completed successfully.$(NC)"

.PHONY: setup

# Deactivate and clean up the virtual environment.
clean:

	@echo "$(GREEN_COLOR)=== Cleaning up the environment ===$(NC)"

	pipenv --rm;

	@echo "$(GREEN_COLOR)Done cleaning$(NC)"

.PHONY: clean

create:
	pip3 install pipenv;

.PHONY: create

# database setup

create-postgres:
	@echo "$(GREEN_COLOR)=== Creating postgres container ===$(NC)"
	@docker-compose -f ./postgres.yml up -d
.PHONY: postgres

delete-postgres:
	@echo "$(GREEN_COLOR)=== Deleting postgres container ===$(NC)"
	@docker-compose -f ./postgres.yml down -v
.PHONY: delete-postgres

reset-postgres: delete-postgres create-postgres
.PHONY: reset-postgres
