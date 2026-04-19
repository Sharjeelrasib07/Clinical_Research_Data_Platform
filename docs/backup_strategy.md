# Backup Strategy

---

## 1. Purpose

This document outlines the approach for backing up data within the platform to ensure data recovery and system reliability.

---

## 2. Scope

This applies to:

- PostgreSQL database
- processed datasets
- critical configuration files

---

## 3. Database Backup

Backups are created using PostgreSQL dump:

```bash
docker compose exec db pg_dump -U postgres research_db > backup.sql