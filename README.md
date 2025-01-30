# API-Testing-Framework
**API Testing Strategy**

## **1. Introduction**
This document outlines the test strategy for API testing in the `API-Testing-Framework` project. The goal is to ensure the reliability, security, and functionality of API endpoints by implementing automated tests using Python, `pytest`, and `requests`.

## **2. Objectives**
- Validate API functionality and responses.
- Ensure API security by testing authentication and authorization.
- Verify data integrity and error handling.
- Automate API test execution using GitHub Actions CI/CD.
- Implement robust error handling for API responses to prevent test failures due to unexpected HTTP responses.

## **3. Scope**
- Testing public API endpoints provided by [ReqRes API](https://reqres.in/).
- Validating HTTP methods: `GET`, `POST`, `PUT`, `DELETE`.
- Ensuring correct response codes and data structure.
- Implementing authentication tests.
- Implementing exception handling for API requests.

## **4. Test Types**
### **4.1 Functional Testing**
- Verify that API endpoints return the expected responses for valid requests.
- Test various HTTP methods and response status codes.

### **4.2 Authentication & Authorization Testing**
- Test login API with valid and invalid credentials.
- Validate token-based authentication for protected endpoints.
- Ensure unauthorized access is properly restricted.

### **4.3 Negative Testing**
- Send invalid data and verify error handling.
- Test endpoints with missing or incorrect authentication.
- Check system behavior when required parameters are missing.

### **4.4 Performance Testing**
- Validate API response times.
- Run multiple requests to evaluate API load handling.

### **4.5 Data Integrity Testing**
- Ensure that data is stored and retrieved correctly.
- Validate the consistency of responses over multiple requests.

### **4.6 Exception Handling & Resilience Testing**
- Implement proper exception handling in API requests.
- Catch and log HTTP errors (4xx, 5xx) instead of failing tests.
- Ensure tests continue running despite transient API failures.

## **5. Test Environment**
- **API Base URL:** `https://reqres.in/api`
- **Tools Used:**
  - `pytest` for test execution.
  - `requests` library for API requests.
  - GitHub Actions for CI/CD.
  - Allure Reports for test reporting (optional).

## **6. Test Execution Plan**
- Tests will be executed locally during development.
- Automated tests will run in GitHub Actions on each `push` and `pull request`.
- Failures will be logged and reported in GitHub Actions.
- API response errors will be properly handled to avoid unnecessary test failures.

## **7. Test Cases Overview**
| **Test Case**                      | **Description**                                | **Expected Outcome** |
|------------------------------------|----------------------------------------------|----------------------|
| GET /users?page=2                  | Retrieve user list                           | 200 OK, valid user data |
| GET /users/{id}                    | Retrieve single user by ID                   | 200 OK, valid user object |
| POST /login (valid)                 | Login with correct credentials               | 200 OK, returns token |
| POST /login (invalid)               | Login with incorrect credentials             | 400 Bad Request, handled gracefully |
| DELETE /posts/{id} (non-existent)   | Delete a non-existing post                   | 204 No Content or 404 Not Found |

## **8. Defect Reporting**
- Any failed tests will be reported in GitHub Actions.
- Critical defects will be logged and documented.
- Issues will be assigned and tracked for resolution.
- API errors will be logged instead of failing tests immediately.

## **9. Risks & Mitigation**
| **Risk**                             | **Mitigation**                           |
|-------------------------------------|------------------------------------------|
| API downtime                        | Implement retry mechanisms for tests.   |
| Inconsistent test results            | Ensure stable test data and assertions. |
| Authentication changes               | Update tests if API authentication changes. |
| Unexpected HTTP errors               | Implement exception handling to prevent test failures. |

## **10. How to Run Tests**
### **10.1 Prerequisites**
Ensure Python and `pytest` are installed:
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### **10.2 Running Tests Locally**
To execute all test cases, run:
```bash
pytest -v
```
To generate an Allure report (if integrated):
```bash
pytest --alluredir=reports/
allure serve reports/
```

### **10.3 Running Tests in GitHub Actions**
Tests are automatically executed in **CI/CD** when pushing code:
1. Commit and push your code:
   ```bash
   git add .
   git commit -m "Updated API test cases"
   git push origin main
   ```
2. Navigate to **GitHub → Actions** tab to view test execution results.

## **11. Conclusion**
This API test strategy ensures a structured approach to validating API functionality, security, and performance. The integration of CI/CD enables continuous testing and immediate feedback on API reliability. By adding exception handling, we improve the resilience of test execution and prevent unnecessary test failures due to API errors.

