.PHONY: help install dev test lint format clean

help:
	@echo "Available commands:"
	@echo "  make install    - Install production dependencies"
	@echo "  make dev        - Install development dependencies"
	@echo "  make test       - Run tests with coverage"
	@echo "  make lint       - Run linting (ruff + mypy)"
	@echo "  make format     - Format code (black + ruff)"
	@echo "  make clean      - Remove build artifacts"

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements.txt -r requirements-dev.txt
	pre-commit install

test:
	pytest tests/ --cov=src/jol_analytics_ai --cov-report=html --cov-report=term-missing

lint:
	ruff check src/ tests/
	mypy src/
	black --check src/ tests/

format:
	black src/ tests/
	ruff check --fix src/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
