
---

# 2. Fill `sop_secure_storage.md`

Paste this:

```markdown
# Standard Operating Procedure (SOP)
## Secure Storage and Data Handling

---

## 1. Purpose

This SOP defines the principles for securely storing and handling pseudonymized research data within the platform.  
Its purpose is to support safe, structured, and reproducible workflows for research-oriented data systems.

---

## 2. Scope

This SOP applies to:

- raw input data
- processed datasets
- PostgreSQL database storage
- application environment variables
- containerized services

All data in this system is synthetic and pseudonymized.

---

## 3. Data Classification

The platform uses pseudonymized research-style data consisting of:

- patient records
- visit data
- laboratory results

No directly identifiable personal information is included.

---

## 4. Storage Layers

### 4.1 Raw Data Layer
Incoming files are stored in:

```text
data/raw/