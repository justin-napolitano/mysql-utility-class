---
slug: github-mysql-utility-class-note-technical-overview
id: github-mysql-utility-class-note-technical-overview
title: mysql-utility-class
repo: justin-napolitano/mysql-utility-class
githubUrl: https://github.com/justin-napolitano/mysql-utility-class
generatedAt: '2025-11-24T18:41:41.414Z'
source: github-auto
summary: >-
  This is a lightweight Python utility for managing MySQL database connections
  and basic operations. It simplifies tasks like connecting to the server and
  creating or dropping databases using environment variables for configuration.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This is a lightweight Python utility for managing MySQL database connections and basic operations. It simplifies tasks like connecting to the server and creating or dropping databases using environment variables for configuration.

## Key Features

- Connect using credentials from environment variables
- Create and drop databases
- Manage connection lifecycle

## Tech Stack

- Python 3.x
- mysql-connector-python
- python-dotenv (for environment vars)

## Getting Started

1. **Clone the repo:**

   ```bash
   git clone https://github.com/justin-napolitano/mysql-utility-class.git
   cd mysql-utility-class
   ```

2. **Install dependencies:**

   ```bash
   pip install mysql-connector-python python-dotenv
   ```

3. **Usage:**

   ```python
   from mysql_utility_class import MySQLConnector

   connector = MySQLConnector()
   connector.connect()
   connector.create_database('test_db')
   connector.drop_database('test_db')
   connector.disconnect()
   ```

### Gotchas

Make sure to set environment variables for `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and optionally `DB_NAME`.
