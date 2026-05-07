# Test Cases Documentation

---

## TC-01: Valid Login

**Test ID:** TC-01  
**Scenario:** TS-01 - User Authentication  
**Title:** Verify user can login with valid credentials  
**Priority:** Critical  
**Type:** Positive / Smoke Test  
**Automated:** Yes → [test_login.py](../tests/test_login.py)

### Preconditions
- User account exists in the system
- Application is accessible

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to /notes/app/login | Login page loads with email and password fields |
| 2 | Enter valid email address | Email field is populated |
| 3 | Enter valid password | Password field is populated (masked) |
| 4 | Click Login button | Form is submitted |
| 5 | Observe page redirect | Redirected to /notes/app dashboard |

### Expected Result
User is successfully logged in and directed to Notes dashboard.

---

## TC-02: Login with Invalid Email

**Test ID:** TC-02  
**Scenario:** TS-02 - Invalid Authentication  
**Title:** Verify login fails with unregistered email  
**Priority:** High  
**Type:** Negative Test  
**Automated:** Yes → [test_login.py](../tests/test_login.py)

### Preconditions
- Application is accessible

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to /notes/app/login | Login page loads |
| 2 | Enter invalid@wrong.com | Email field is populated |
| 3 | Enter any password | Password field is populated |
| 4 | Click Login button | Form is submitted |
| 5 | Observe page behavior | Error message shown OR still on login page |

### Expected Result
Login fails and user remains on login page with error message.

---

## TC-03: Login with Wrong Password

**Test ID:** TC-03  
**Scenario:** TS-03 - Invalid Credentials  
**Title:** Verify login fails with incorrect password  
**Priority:** High  
**Type:** Negative Test  
**Automated:** Yes → [test_login.py](../tests/test_login.py)

### Preconditions
- User account exists with known email
- Application is accessible

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to /notes/app/login | Login page loads |
| 2 | Enter valid registered email | Email field is populated |
| 3 | Enter incorrect password | Password field is populated |
| 4 | Click Login button | Form is submitted |
| 5 | Observe result | Login fails, error message displayed |

### Expected Result
Login fails and error message is shown to user.

---

## TC-04: Login with Empty Email

**Test ID:** TC-04  
**Scenario:** TS-04 - Empty Fields  
**Title:** Verify login fails with empty email field  
**Priority:** Medium  
**Type:** Negative Test  
**Automated:** Yes → [test_login.py](../tests/test_login.py)

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to /notes/app/login | Login page loads |
| 2 | Leave email field empty | Email field is empty |
| 3 | Enter password | Password field is populated |
| 4 | Click Login button | Form submission is blocked |

### Expected Result
Login fails with validation message. User remains on login page.

---

## TC-05: Login with Empty Password

**Test ID:** TC-05  
**Scenario:** TS-04 - Empty Fields  
**Title:** Verify login fails with empty password field  
**Priority:** Medium  
**Type:** Negative Test  
**Automated:** Yes → [test_login.py](../tests/test_login.py)

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to /notes/app/login | Login page loads |
| 2 | Enter email address | Email field is populated |
| 3 | Leave password field empty | Password field is empty |
| 4 | Click Login button | Form submission is blocked |

### Expected Result
Login fails with validation message.

---

## TC-06: Both Fields Empty

**Test ID:** TC-06  
**Scenario:** TS-04 - Empty Fields  
**Title:** Verify login fails with both fields empty  
**Priority:** Medium  
**Type:** Negative Test  
**Automated:** Yes → [test_login.py](../tests/test_login.py)

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to /notes/app/login | Login page loads |
| 2 | Leave both fields empty | Email and password fields are empty |
| 3 | Click Login button | Form submission is blocked |

### Expected Result
Login fails. User remains on login page with validation errors.

---

## TC-07: Login Page Elements Display

**Test ID:** TC-07  
**Scenario:** TS-01 - Page Elements  
**Title:** Verify all login page elements are present  
**Priority:** High  
**Type:** Positive Test  
**Automated:** Yes → [test_login.py](../tests/test_login.py)

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to /notes/app/login | Login page loads |
| 2 | Verify page elements | Email input field visible |
| 3 | Verify page elements | Password input field visible |
| 4 | Verify page elements | Login button visible |
| 5 | Verify page elements | Register link visible |

### Expected Result
All required login page elements are visible and functional.

---

## TC-08: Create Note - Home Category

**Test ID:** TC-08  
**Scenario:** TS-06 - Note Creation  
**Title:** Create note with Home category  
**Priority:** Critical  
**Type:** Positive / Smoke Test  
**Automated:** Yes → [test_notes_ui.py](../tests/test_notes_ui.py)

### Preconditions
- User is logged in
- Notes dashboard is displayed

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Add New Note" button | Note creation modal opens |
| 2 | Select category "Home" | Home category is selected |
| 3 | Enter note title | Title field is populated |
| 4 | Enter note description | Description field is populated |
| 5 | Click Create/Save button | Form is submitted |
| 6 | Observe dashboard | New note card appears in dashboard |

### Expected Result
Note is created successfully with Home category and appears on dashboard.

---

## TC-09: Create Note - Work Category

**Test ID:** TC-09  
**Scenario:** TS-07 - Note Creation  
**Title:** Create note with Work category  
**Priority:** Critical  
**Type:** Positive Test  
**Automated:** Yes → [test_notes_ui.py](../tests/test_notes_ui.py)

### Preconditions
- User is logged in
- Notes dashboard is displayed

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Add New Note" button | Note creation form opens |
| 2 | Select category "Work" | Work category is selected |
| 3 | Enter note title | Title field is populated |
| 4 | Enter note description | Description field is populated |
| 5 | Click Create button | Note is created and saved |
| 6 | Observe dashboard | New note appears in dashboard |

### Expected Result
Note is created successfully with Work category.

---

## TC-10: Create Note - Personal Category

**Test ID:** TC-10  
**Scenario:** TS-08 - Note Creation  
**Title:** Create note with Personal category  
**Priority:** Critical  
**Type:** Positive Test  
**Automated:** Yes → [test_notes_ui.py](../tests/test_notes_ui.py)

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Add New Note" button | Note creation form opens |
| 2 | Select category "Personal" | Personal category is selected |
| 3 | Enter note title | Title field is populated |
| 4 | Enter note description | Description field is populated |
| 5 | Click Create button | Note is created |
| 6 | Verify on dashboard | New note appears on dashboard |

### Expected Result
Note is created successfully with Personal category.

---

## TC-11: Get All Notes via API

**Test ID:** TC-11  
**Scenario:** TS-11 - API Read Operations  
**Title:** GET /notes returns list of user notes  
**Priority:** Critical  
**Type:** Positive Test  
**Automated:** Yes → [test_notes_api.py](../tests/test_notes_api.py)

### Preconditions
- User is authenticated
- API token is valid

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Call GET /notes endpoint | Request is sent with auth token |
| 2 | Observe HTTP response | Status code 200 OK |
| 3 | Verify response body | List of notes returned |
| 4 | Verify schema | Response contains required fields |

### Expected Result
API returns 200 OK with list of user notes.

---

## TC-12: Create Note via API

**Test ID:** TC-12  
**Scenario:** TS-12 - API Write Operations  
**Title:** POST /notes creates new note  
**Priority:** Critical  
**Type:** Positive Test  
**Automated:** Yes → [test_notes_api.py](../tests/test_notes_api.py)

### Preconditions
- User is authenticated
- Valid auth token available

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send POST request to /notes | Request includes title and description |
| 2 | Include note data in body | Category, title, description provided |
| 3 | Include auth token in header | Authorization header present |
| 4 | Observe response | Status code 201 Created |
| 5 | Verify response body | Note ID and data returned |

### Expected Result
Note is created successfully via API. Returns 201 with note details.

---

## TC-13: Delete Note via API

**Test ID:** TC-13  
**Scenario:** TS-15 - API Delete Operations  
**Title:** DELETE /notes/{id} removes note  
**Priority:** High  
**Type:** Positive Test  
**Automated:** Yes → [test_notes_api.py](../tests/test_notes_api.py)

### Preconditions
- User is authenticated
- Note with valid ID exists

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Get note ID | Note ID is obtained |
| 2 | Send DELETE request | DELETE /notes/{id} endpoint called |
| 3 | Include auth token | Authorization header present |
| 4 | Observe response | Status code 200 OK or 204 |
| 5 | Verify deletion | Note no longer exists in API |

### Expected Result
Note is deleted successfully. API returns success status.

---

## TC-14: API - Unauthorized Request

**Test ID:** TC-14  
**Scenario:** TS-16 - API Error Handling  
**Title:** GET /notes returns 401 without authentication  
**Priority:** High  
**Type:** Negative Test  
**Automated:** Yes → [test_notes_api.py](../tests/test_notes_api.py)

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to /notes | No auth token provided |
| 2 | Omit authorization header | Request without authentication |
| 3 | Observe response | Status code 401 Unauthorized |
| 4 | Verify error message | Error message indicates auth required |

### Expected Result
API returns 401 Unauthorized when no auth token provided.

---

## TC-15: Delete Non-existent Note

**Test ID:** TC-15  
**Scenario:** TS-17 - API Error Handling  
**Title:** DELETE /notes/{id} with invalid ID returns error  
**Priority:** High  
**Type:** Negative Test  
**Automated:** Yes → [test_notes_api.py](../tests/test_notes_api.py)

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Prepare invalid note ID | Use non-existent ID |
| 2 | Send DELETE request | DELETE /notes/{invalid_id} called |
| 3 | Include auth token | Valid authorization provided |
| 4 | Observe response | Status code 404 Not Found |
| 5 | Verify error | Error message about not found |

### Expected Result
API returns 404 Not Found error.

---

## TC-16: UI-API Data Consistency

**Test ID:** TC-16  
**Scenario:** TS-18 - End-to-End Testing  
**Title:** Note created in UI appears in API response  
**Priority:** High  
**Type:** E2E Test  
**Automated:** Yes → [test_e2e.py](../tests/test_e2e.py)

### Preconditions
- User is logged in via UI
- User is authenticated via API

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create note via UI | Note title: "E2E Test Note" |
| 2 | Note appears on dashboard | Note is visible in UI |
| 3 | Call API GET /notes | Retrieve notes via API |
| 4 | Search response for note | Note should exist in API response |
| 5 | Compare data | Title and description match |

### Expected Result
Note created in UI matches the data returned from API.

---

## TC-17: API-to-UI Sync

**Test ID:** TC-17  
**Scenario:** TS-21 - End-to-End Testing  
**Title:** Note created via API appears in UI  
**Priority:** High  
**Type:** E2E Test  
**Automated:** Yes → [test_e2e.py](../tests/test_e2e.py)

### Preconditions
- User is logged in via UI
- User is authenticated via API

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create note via API | Note is created successfully |
| 2 | Refresh UI dashboard | Dashboard is refreshed |
| 3 | Observe notes list | New note appears in dashboard |
| 4 | Verify note details | Title and description are correct |

### Expected Result
Note created via API appears on UI dashboard after refresh.

---

## TC-18: API Health Check

**Test ID:** TC-18  
**Scenario:** TS-26 - API Health  
**Title:** API health check returns 200 status  
**Priority:** Critical  
**Type:** Smoke Test  
**Automated:** Yes → [test_notes_api.py](../tests/test_notes_api.py)

### Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Call GET /health endpoint | Request sent |
| 2 | Observe response | Status code 200 OK |
| 3 | Verify response | JSON body with status |

### Expected Result
API health endpoint returns 200 OK.

---

## Summary

- **Total Test Cases:** 18
- **UI Tests:** 8
- **API Tests:** 7
- **E2E Tests:** 2
- **Positive Tests:** 14
- **Negative Tests:** 4
- **Automation:** 100% Automated

---

## TC-05: Note Count Increases After Creation

| Field             | Details                                                          |
|-------------------|------------------------------------------------------------------|
| Test Case ID      | TC-05                                                            |
| Title             | Verify note count increases by 1 after creating note             |
| Type              | Positive / Regression                                            |
| Automated         | Yes → test_notes_ui.py::test_note_appears_instantly_after_creation|

| Step | Action                              | Expected Result                              |
|------|-------------------------------------|----------------------------------------------|
| 1    | Record current note count           | Count N captured                             |
| 2    | Create one new note                 | Note submitted                               |
| 3    | Count notes on dashboard            | Count is now N+1                             |

---

## TC-06: GET /notes API Returns 200

| Field             | Details                                             |
|-------------------|-----------------------------------------------------|
| Test Case ID      | TC-06                                               |
| Title             | GET /notes returns 200 with user's note list        |
| Priority          | Critical                                            |
| Type              | API / Smoke                                         |
| Automated         | Yes → test_notes_api.py::TestNotesAPI::test_get_all_notes |

**Preconditions:** User is authenticated (token available).

| Step | Action                                      | Expected Result                    |
|------|---------------------------------------------|------------------------------------|
| 1    | Register and login via API                  | Token obtained                     |
| 2    | Send GET /notes with x-auth-token header    | Request sent                       |
| 3    | Check response status code                  | 200 OK                             |
| 4    | Check response body                         | success=true, data=array           |

---

## TC-07: DELETE /notes/{id} Removes Note

| Field             | Details                                             |
|-------------------|-----------------------------------------------------|
| Test Case ID      | TC-07                                               |
| Title             | Delete note via API and verify it no longer exists  |
| Priority          | Critical                                            |
| Type              | API / Smoke                                         |
| Automated         | Yes → test_notes_api.py::TestNotesAPI::test_delete_note_api |

| Step | Action                                      | Expected Result                    |
|------|---------------------------------------------|------------------------------------|
| 1    | Create note via POST /notes                 | Note created, ID captured          |
| 2    | Send DELETE /notes/{id}                     | 200 OK returned                    |
| 3    | Send GET /notes/{id}                        | 404 or error response              |

---

## TC-08: API Response Time < 2 Seconds

| Field             | Details                                                |
|-------------------|--------------------------------------------------------|
| Test Case ID      | TC-08                                                  |
| Title             | Verify GET /notes response time is under 2 seconds     |
| Type              | Performance                                            |
| Automated         | Yes → test_notes_api.py::test_get_notes_response_time  |

| Step | Action                         | Expected Result              |
|------|--------------------------------|------------------------------|
| 1    | Login via API                  | Token obtained               |
| 2    | Record timestamp               | Start time captured          |
| 3    | Send GET /notes                | Response received            |
| 4    | Measure elapsed time           | elapsed < 2.0 seconds        |

---

## TC-09: UI → API Data Consistency (E2E Scenario 1)

| Field             | Details                                                     |
|-------------------|-------------------------------------------------------------|
| Test Case ID      | TC-09                                                       |
| Title             | Note created in UI matches data fetched via API             |
| Priority          | Critical                                                    |
| Type              | E2E / Smoke                                                 |
| Automated         | Yes → test_e2e.py::TestE2E::test_ui_create_api_verify       |

| Step | Action                                | Expected Result                         |
|------|---------------------------------------|-----------------------------------------|
| 1    | Login to app (UI + API)               | Both sessions authenticated             |
| 2    | Create note via UI with known title   | Note appears on UI dashboard            |
| 3    | Call GET /notes via API               | 200 response with notes list            |
| 4    | Find note by title in API response    | Note found in API data                  |
| 5    | Compare title, description, category  | All fields match between UI and API     |

---

## TC-10: API Delete Removes Note from UI (E2E Scenario 2)

| Field             | Details                                                     |
|-------------------|-------------------------------------------------------------|
| Test Case ID      | TC-10                                                       |
| Title             | Note deleted via API disappears from UI after refresh       |
| Priority          | Critical                                                    |
| Type              | E2E / Smoke                                                 |
| Automated         | Yes → test_e2e.py::TestE2E::test_api_delete_ui_verify       |

| Step | Action                                | Expected Result                         |
|------|---------------------------------------|-----------------------------------------|
| 1    | Create note via API                   | Note created, ID captured               |
| 2    | Refresh browser                       | Note appears in UI dashboard            |
| 3    | Delete note via DELETE /notes/{id}    | 200 OK response                         |
| 4    | Refresh UI page                       | Note list reloads                       |
| 5    | Search for deleted note title         | Note NOT found in UI                    |

---

## TC-11: Unauthorized Access Returns 401

| Field             | Details                                                     |
|-------------------|-------------------------------------------------------------|
| Test Case ID      | TC-11                                                       |
| Title             | Accessing /notes without token returns 401                  |
| Type              | Negative / API                                              |
| Automated         | Yes → test_notes_api.py::test_get_notes_without_auth        |

| Step | Action                              | Expected Result              |
|------|-------------------------------------|------------------------------|
| 1    | Do NOT login (no token)             | No x-auth-token header       |
| 2    | Send GET /notes                     | Request sent without auth    |
| 3    | Check status code                   | 401 Unauthorized             |
