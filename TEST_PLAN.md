# Test Plan: Wacky Widget Organization Management System

**Project:** Wacky Widget Organization Management System  
**Testing Team:** Team 2  
**Date:** November 13, 2025  
**Version:** 1.0

---

## 1. SCOPE (5 points)

### 1.1 In Scope
- All core HR operations (HIRE, FIRE, QUIT, LAYOFF, TRANSFER, PROMOTE)
- Organization hierarchy management (President → VP → Supervisor → Worker)
- Capacity constraints for each role level
- Vacancy handling and tracking
- Name uniqueness validation
- Display functionality for organization chart
- Command-line interface and user interactions
- Error handling and user feedback messages

### 1.2 Out of Scope
- File import/export functionality (Requirement 9 - not implemented in code)
- Performance testing with large organizations
- Concurrent user access
- Database persistence
- GUI interface
- Authentication/authorization
- Multi-language support

### 1.3 Testing Objectives
- Verify all functional requirements per SRS are correctly implemented
- Identify defects through systematic black-box testing
- Validate business rules and constraints
- Ensure appropriate error handling and user feedback
- Assess system readiness for production deployment

---

## 2. TEST STRATEGY (50 points)

### 2.1 Testing Approach
**Black Box Testing** will be employed exclusively, focusing on:
- **Equivalence Partitioning:** Group inputs into valid/invalid classes
- **Boundary Value Analysis:** Test limits of capacity constraints (0, 1, max, max+1)
- **Decision Table Testing:** Complex business rules (layoff placement, promotion eligibility)
- **State Transition Testing:** Employee movement through hierarchy
- **Error Guessing:** Edge cases based on requirements ambiguities

### 2.2 Test Levels
1. **Functional Testing:** Verify each command works per specification
2. **Integration Testing:** Test interactions between commands (e.g., FIRE then HIRE)
3. **Negative Testing:** Invalid inputs, constraint violations
4. **Usability Testing:** Error messages, command syntax validation

### 2.3 Test Categories

#### Category A: Initialization & Setup
- President initialization
- Name validation rules
- Empty organization state

#### Category B: Hierarchy Operations
- **HIRE:** Direct hiring under managers at all levels
- **FIRE:** Removal with vacancy creation
- **QUIT:** Self-initiated departure
- **LAYOFF:** Removal with relocation attempt
- **TRANSFER:** Lateral moves within hierarchy
- **PROMOTE:** Upward movement one level

#### Category C: Capacity Management
- Maximum direct reports per role (President: 2, VP: 3, Supervisor: 5)
- Vacancy filling
- Capacity validation during operations

#### Category D: Authorization & Hierarchy Rules
- Firing within hierarchy only
- Transfer authorization (VP/President only)
- Promotion receiving manager eligibility
- Peer supervision prevention

#### Category E: Vacancy Handling
- Vacancy creation on departure
- Vacancy filling on hire
- Reporting to vacant positions
- Display of vacancies (supervisory only)

#### Category F: Display & Output
- Organization chart formatting
- Vacancy display rules
- Empty organization handling
- Indentation and hierarchy visualization

#### Category G: Edge Cases & Error Handling
- Duplicate names
- Non-existent employees
- Invalid command syntax
- Workers attempting to hire
- President special cases (cannot quit/fire)
- Multi-level promotion attempts

### 2.4 Test Data Strategy
- **Minimal Organization:** President only
- **Small Organization:** President + 1-2 VPs + few supervisors
- **Full Organization:** All positions filled to capacity
- **Sparse Organization:** Many vacancies
- **Edge Names:** Empty strings, spaces, special characters, very long names

### 2.5 Pass/Fail Criteria
- **Pass:** Expected output matches actual output, correct state changes, appropriate error messages
- **Fail:** Incorrect behavior, crashes, missing validation, wrong error messages, data corruption

---

## 3. RESOURCES (5 points)

### 3.1 Human Resources
- **Test Team:** 4 testers working collaboratively
- **Developer Contact:** Available for blocking bugs only
- **Time Allocation per Tester:** ~5-7 hours total
- **Total Team Effort:** ~20-25 hours

### 3.2 Technical Resources
- **Hardware:** Windows PC
- **Software:** 
  - Python 3.x
  - pytest testing framework
  - VS Code or similar IDE
  - Git for version control
- **Test Environment:** Local development machine
- **Test Tools:** 
  - Manual testing via command line
  - Automated test execution via pytest
  - Output capture for verification

### 3.3 Test Artifacts
- Test plan document (this document)
- Test case specifications
- Test execution results log
- Bug reports
- Quality assessment report

---

## 4. TIMELINE (10 points)

### Phase 1: Planning & Design (1 hour per tester, parallel)
- Review SRS and code structure
- Create test plan collaboratively
- Divide test case design responsibilities
- Set up test environments

### Phase 2: Test Case Development (1 hour per tester, parallel)
- **Tester 1:** HIRE, FIRE operations
- **Tester 2:** QUIT, LAYOFF operations  
- **Tester 3:** TRANSFER, PROMOTE operations
- **Tester 4:** DISPLAY, Initialization, Edge cases
- Document expected results
- Peer review test cases

### Phase 3: Test Execution - Pass 1 (2 hours per tester, parallel)
- Execute assigned test categories
- Document results in shared tracker
- Log defects with unique IDs
- Identify blocking issues

### Phase 4: Bug Reporting & Developer Communication (30 min per tester)
- Consolidate and deduplicate bug reports
- Prioritize bugs as team
- Communicate blocking bugs
- Wait for critical fixes

### Phase 5: Test Execution - Pass 2 (1 hour per tester, parallel)
- Regression testing on fixed bugs
- Cross-test other categories
- Execute edge case scenarios

### Phase 6: Test Execution - Pass 3 (Optional, 1 hour per tester)
- Final verification pass
- Exploratory testing
- Boundary condition deep dive

### Phase 7: Reporting & Assessment (30 min per tester, collaborative)
- Compile test results
- Finalize bug reports as team
- Write quality assessment collaboratively
- Prepare deliverables

**Total Estimated Time per Tester:** 5-7 hours over 1 week  
**Total Team Effort:** 20-28 hours

---

## 5. RISKS & MITIGATION (10 points)

### 5.1 Risk: Blocking Bugs
- **Impact:** HIGH - Could halt all testing
- **Probability:** MEDIUM
- **Mitigation:** 
  - Identify critical path tests early
  - Contact developer immediately for blocking bugs
  - Have alternate test scenarios ready
  - Document blocking impact thoroughly

### 5.2 Risk: Incomplete/Ambiguous Requirements
- **Impact:** MEDIUM - May test wrong behavior
- **Probability:** HIGH
- **Mitigation:**
  - Document all assumptions
  - Ask developer for clarification on ambiguities
  - Test both interpretations when unclear
  - Note requirement gaps in quality assessment

### 5.3 Risk: Inadequate Test Coverage
- **Impact:** HIGH - May miss critical bugs
- **Probability:** MEDIUM
- **Mitigation:**
  - Use systematic test design techniques
  - Perform requirements traceability
  - Conduct exploratory testing sessions
  - Peer review test cases

### 5.4 Risk: Time Constraints
- **Impact:** MEDIUM - May not complete all testing
- **Probability:** MEDIUM
- **Mitigation:**
  - Prioritize critical/high-risk areas
  - Focus on core functionality first
  - Use automated test execution where possible
  - Track time spent per category

### 5.5 Risk: Test Environment Issues
- **Impact:** LOW - Setup problems
- **Probability:** LOW
- **Mitigation:**
  - Verify Python and dependencies early
  - Test basic execution before detailed testing
  - Have backup environment ready

### 5.6 Risk: Misunderstanding Developer's Implementation
- **Impact:** MEDIUM - False positives/negatives
- **Probability:** MEDIUM
- **Mitigation:**
  - Black box focus - test against SRS only
  - Document deviations from expected behavior
  - Request developer addendum/clarifications
  - Cross-reference with existing unit tests

### 5.7 Risk: Data Corruption Between Tests
- **Impact:** HIGH - Invalid test results
- **Probability:** LOW
- **Mitigation:**
  - Reset organization state between tests
  - Use fresh instances for each test
  - Verify initial state before each test
  - Document state dependencies



