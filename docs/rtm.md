# Requirement Traceability Matrix (RTM)

## Overview
This matrix maps business requirements to test scenarios and automated test cases for the Notes Application testing framework.

## Key Definitions

| Term | Meaning |
|------|---------|
| **REQ** | Business Requirement ID |
| **TS** | Test Scenario ID |
| **TC** | Test Case ID (code method name) |
| **Status** | Automated / Manual / Planned |

---

## UI Login Requirements

| Req ID | Requirement | Test Scenario | Test Case | Priority |
|--------|-------------|---------------|-----------|----------|
| REQ-01 | User can login with valid credentials | TS-01 | test_valid_login | Critical |
| REQ-02 | Login redirects to notes dashboard | TS-05 | test_login_redirects_to_notes | High |
| REQ-03 | Login fails with invalid email | TS-02 | test_invalid_email | High |
| REQ-04 | Login fails with wrong password | TS-03 | test_invalid_password | High |
| REQ-05 | Login fails with empty email | TS-04 | test_empty_email | Medium |
| REQ-06 | Login fails with empty password | TS-04 | test_empty_password | Medium |
| REQ-07 | Login fails with both fields empty | TS-04 | test_both_fields_empty | Medium |
| REQ-08 | Login page shows all required elements | TS-01 | test_login_page_elements_displayed | High |

---

## UI Note Operations Requirements

| Req ID | Requirement | Test Scenario | Test Case | Priority |
|--------|-------------|---------------|-----------|----------|
| REQ-09 | Create note with Home category | TS-06 | test_create_note_home_category | Critical |
| REQ-10 | Create note with Work category | TS-07 | test_create_note_work_category | Critical |
| REQ-11 | Create note with Personal category | TS-08 | test_create_note_personal_category | Critical |
| REQ-12 | Note appears immediately after creation | TS-09 | test_note_appears_instantly | High |
| REQ-13 | Create and display multiple notes | TS-10 | test_multiple_notes_creation | High |
| REQ-14 | Delete note via UI | TS-10 | test_delete_note_via_ui | High |

---

## API CRUD Operations Requirements

| Req ID | Requirement | Test Scenario | Test Case | Priority |
|--------|-------------|---------------|-----------|----------|
| REQ-15 | API health check returns 200 | TS-26 | test_api_health_check | Critical |
| REQ-16 | GET /notes returns 200 | TS-11 | test_get_all_notes | Critical |
| REQ-17 | GET /notes returns list of notes | TS-11 | test_get_notes_returns_list | High |
| REQ-18 | POST /notes creates note | TS-12 | test_create_note_api | Critical |
| REQ-19 | GET /notes/{id} retrieves note | TS-13 | test_get_note_by_id | High |
| REQ-20 | DELETE /notes/{id} removes note | TS-15 | test_delete_note_api | High |
| REQ-21 | PUT /notes/{id} updates note | TS-14 | test_update_note_api | High |

---

## API Error Handling Requirements

| Req ID | Requirement | Test Scenario | Test Case | Priority |
|--------|-------------|---------------|-----------|----------|
| REQ-22 | GET /notes returns 401 without auth | TS-16 | test_get_notes_without_auth | High |
| REQ-23 | Delete non-existent note returns error | TS-17 | test_delete_nonexistent_note | High |

---

## API Response Validation Requirements

| Req ID | Requirement | Test Scenario | Test Case | Priority |
|--------|-------------|---------------|-----------|----------|
| REQ-24 | Note response has required fields | TS-25 | test_note_response_schema | High |

---

## Performance Requirements

| Req ID | Requirement | Test Scenario | Test Case | Priority |
|--------|-------------|---------------|-----------|----------|
| REQ-25 | GET /notes response time < 2 seconds | TS-22 | test_get_notes_response_time | Medium |
| REQ-26 | POST /notes response time < 2 seconds | TS-23 | test_create_note_response_time | Medium |
| REQ-32 | UI page load time < 5 seconds | TS-24 | test_ui_page_load_performance | Medium |

---

## End-to-End (E2E) Requirements

| Req ID | Requirement | Test Scenario | Test Case | Priority |
|--------|-------------|---------------|-----------|----------|
| REQ-27 | Note created in UI matches API data | TS-18 | test_ui_create_api_verify | High |
| REQ-28 | Note data consistent UI and API | TS-19 | test_ui_create_api_verify | High |
| REQ-29 | Note deleted via API disappears from UI | TS-20 | test_api_delete_ui_verify | High |
| REQ-30 | API-created note appears in UI | TS-21 | test_api_delete_ui_verify | High |
| REQ-31 | Full CRUD cycle works across UI and API | TS-18-21 | test_full_crud_hybrid | Critical |

---

## Coverage Summary

| Category | Requirements | Automated | Status |
|----------|--------------|-----------|--------|
| UI Login | 8 | 8 | 100% |
| UI Notes | 6 | 6 | 100% |
| API CRUD | 7 | 7 | 100% |
| API Error | 2 | 2 | 100% |
| API Schema | 1 | 1 | 100% |
| Performance | 3 | 3 | 100% |
| E2E Tests | 5 | 5 | 100% |
| **TOTAL** | **32** | **32** | **100%** |
