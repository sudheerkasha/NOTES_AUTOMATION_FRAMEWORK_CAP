# Test Plan - Notes Application

## 1. Project Overview

**Application:** Notes Application  
**URL:** https://practice.expandtesting.com/notes/app  
**API Base:** https://practice.expandtesting.com/notes/api

This document outlines the complete testing strategy for the Notes Application using a hybrid Selenium + Python + Pytest automation framework.

---

## 2. Test Objectives

- Validate user login functionality (positive and negative scenarios)
- Verify note CRUD operations via UI
- Verify note CRUD operations via API
- Ensure data consistency between UI and API
- Validate API performance (response time < 2 seconds)
- Test error handling and edge cases
- Generate automated Allure reports

---

## 3. Scope

### In Scope
- User authentication (login/register)
- Note creation, reading, updating, deletion
- UI-API data consistency
- API response validation
- Error handling and negative testing
- Performance testing

### Out of Scope
- Password reset flows (requires email verification)
- Load/stress testing
- Mobile responsiveness
- Browser compatibility beyond Chrome, Firefox, Edge

---

## 4. Test Environment

| Component | Details |
|-----------|---------|
| **OS** | Windows 10/11 |
| **Python** | 3.10+ |
| **Browsers** | Chrome, Firefox, Edge |
| **Selenium** | 4.x |
| **Pytest** | 7.x |
| **Reporting** | Allure Reports |
| **API Testing** | Requests library |
| **Logging** | Colorlog |
| **Test Data** | Faker library |

---

## 5. Test Strategy

### Test Types

| Type | Tool | Purpose |
|------|------|---------|
| **UI Tests** | Selenium WebDriver | Login, note CRUD via browser |
| **API Tests** | Requests library | REST API CRUD, authentication |
| **E2E Tests** | Selenium + Requests | Cross-layer data consistency |
| **Performance** | Response time assertions | API < 2s, UI load < 5s |

### Test Levels

| Level | Description | Coverage |
|-------|-------------|----------|
| **Smoke** | Critical functionality | Login + create note + API health |
| **Regression** | Complete test suite | All modules and scenarios |
| **Negative** | Error scenarios | Invalid inputs, auth failures |

### Markers Used

```
@pytest.mark.smoke       - Critical path tests
@pytest.mark.ui          - UI tests
@pytest.mark.api         - API tests
@pytest.mark.regression  - Full regression suite
@pytest.mark.negative    - Error/negative tests
@pytest.mark.e2e         - End-to-end tests
@pytest.mark.performance - Performance tests
```

---

## 6. Test Execution

### Local Execution
```bash
pytest tests/ -v
pytest tests/test_login.py -v
pytest tests/ -m smoke
pytest tests/ -m regression
```

### Parallel Execution
```bash
pytest tests/ -n 4
```

### With Allure Reports
```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

### CI/CD Pipeline
- Executed via Jenkins
- Runs on every commit
- Generates Allure reports
- Archives test artifacts

---

## 7. Entry Criteria

Before testing can begin:
- Application deployed and accessible
- API health check returns 200 OK
- Test environment configured
- Test user credentials available
- Browser drivers installed

---

## 8. Exit Criteria

Testing is complete when:
- All smoke tests pass (100%)
- Regression test pass rate ≥ 95%
- No critical/blocker defects open
- Allure report generated
- Test logs and artifacts archived

---

## 9. Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Flaky UI elements | Medium | Self-healing locators + retry logic |
| Network latency | Medium | Configurable timeouts + retries |
| Test data conflicts | Low | Unique data per test + cleanup |
| API breaking changes | High | Schema validation + API monitoring |

---

## 10. Test Deliverables

- Test Plan (this document)
- Test Cases documentation
- Test Scenarios documentation
- Requirement Traceability Matrix (RTM)
- Automated test scripts
- Allure test reports
- Test execution logs

---

## 11. Success Metrics

| Metric | Target |
|--------|--------|
| Test Coverage | 100% |
| Automation Coverage | 100% |
| Pass Rate | 95%+ |
| Defect Detection Rate | High |
| Test Execution Time | < 5 minutes |
| API Response Time | < 2 seconds |
| UI Page Load Time | < 5 seconds |

---

## 12. Test Team

| Role | Responsibility |
|------|-----------------|
| Test Automation Lead | Framework setup, script maintenance |
| QA Engineer | Test case creation, execution |
| DevOps | CI/CD pipeline, environment setup |
- Test Scenarios and Test Cases
- Requirement Traceability Matrix (RTM)
- Automation framework with full code
- Allure test execution reports
- Jenkins CI/CD pipeline configuration
