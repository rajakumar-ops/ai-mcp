# Leave Manager MCP

A simple employee leave management system built with MCP (Modern Concurrency Platform).

## Overview

Leave Manager MCP is a lightweight application that helps track employee leave balances and leave history. It provides an API to view, request, and manage employee time off.

## Features

- View employee leave balances
- Check leave history for employees
- Request time off
- Approve/deny leave requests
- Track remaining leave days

## Requirements

- Python 3.13+
- MCP 1.13.0+

## Installation
## Installation

1. Clone this repository
2. Install dependencies:

```bash
uv run mcp install main.py



1. Clone this repository
2. Install dependencies:

```bash
uv pip install -e .
```

## Usage

Run the application:

```bash
python main.py
```

The server will start and be available at http://localhost:8000

## API Endpoints

- GET `/employee/{name}/leaves` - Get leave information for an employee
- POST `/employee/{name}/request` - Request leave for an employee
- GET `/employees` - List all employees

## Development

This project uses uv for dependency management and pyproject.toml for package configuration.

## License

MIT
