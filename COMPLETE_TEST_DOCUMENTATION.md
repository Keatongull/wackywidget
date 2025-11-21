# Wacky Widget Organization Management System - Complete Test Documentation

**Project:** Wacky Widget Organization Management System  
**Testing Team:** Team 2  
**Date:** November 20, 2025  
**Version:** 1.1

---

# Table of Contents

1. [Test Plan](#test-plan)
   - [Scope](#1-scope-5-points)
   - [Test Strategy](#2-test-strategy-50-points)
   - [Resources](#3-resources-5-points)
   - [Timeline](#4-timeline-10-points)
   - [Risks & Mitigation](#5-risks--mitigation-10-points)
   - [Automated Testing Implementation](#6-automated-testing-implementation-20-points)
2. [Test Cases](#test-cases)
   - [Test Suite Overview](#test-suite-overview)
   - [Detailed Test Case Specifications](#detailed-test-case-specifications)
3. [Test Results](#test-results)
   - [Test Summary](#2-test-summary)
   - [Detailed Results](#3-detailed-test-results)
   - [Specification Bugs](#4-specification-bugs)
   - [Bug Summary](#5-bug-summary)
   - [Final Quality Assessment](#7-final-assessment-of-quality)

---

# Test Plan

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

The test suite covers 150 automated test cases organized into the following categories:

#### Category A: Initialization & Setup (6 tests)
- President initialization with valid/invalid names
- Name validation rules (spaces, empty, numeric, special characters)
- Empty organization state
- Invalid name reprompting behavior

#### Category B: HIRE Operations (13 tests)
- Direct hiring under managers at all levels
- Capacity enforcement (President: 2, VP: 3, Supervisor: 5)
- Worker hiring restrictions
- Duplicate name detection and validation
- Invalid manager validation

#### Category C: FIRE Operations (5 tests)
- Removal with vacancy creation
- Firing employees with and without reports
- President protection (cannot be fired)
- Hierarchy enforcement
- Non-existent employee handling

#### Category D: QUIT Operations (8 tests)
- Self-initiated departure
- President quit restriction
- Subordinate preservation after quit
- Case sensitivity in names

#### Category E: LAYOFF Operations (4 tests)
- Removal with relocation attempt
- Placement in available positions
- President layoff restriction
- Subordinate handling during layoff

#### Category F: TRANSFER Operations (4 tests)
- Lateral moves within hierarchy
- Transfer authorization (VP/President only)
- Cross-hierarchy transfers
- Capacity validation

#### Category G: PROMOTE Operations (6 tests)
- Upward movement one level (Worker→Supervisor, Supervisor→VP)
- Multi-level promotion prevention
- VP promotion limit
- Vacancy requirement
- Receiving manager eligibility

#### Category H: DISPLAY Operations (3 tests)
- Organization chart formatting and visualization
- Vacancy display rules (supervisory only)
- Empty organization handling
- Indentation and hierarchy visualization

#### Category I: Edge Cases & Integration (31 tests)
- Vacancy filling scenarios
- Complex multi-operation workflows
- Maximum capacity scenarios
- Promoted employee capacity changes
- Transfer and promote combinations
- Deep hierarchy operations

#### Category J: Bug Detection Tests (70 tests)
- Subordinate visibility after manager removal
- Promotion system defects and hierarchy violations
- Name validation edge cases
- Vacancy management and display issues
- Capacity enforcement bypass scenarios
- Operation combinations and state transitions

### 2.4 Test Data Strategy

#### Organization Sizes
- **Minimal:** President only (initialization tests)
- **Small:** 1-2 VPs with sparse reporting structure
- **Medium:** Multiple VPs with several supervisors
- **Full:** All positions at maximum capacity
- **Deep:** Maximum nesting depth with vacancies

#### Name Variations
- Valid alphabetic names (Alice, Bob, President1)
- Single character and very long names (100+ characters)
- Case variations (PRESIDENT, president, AlIcE)
- Invalid formats (numeric, spaces, special characters, escape sequences)
- Edge cases (empty, command words, SQL injection attempts)

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

---

## 6. AUTOMATED TESTING IMPLEMENTATION (20 points)

### 6.1 Overview
An automated black-box test suite has been developed to systematically verify the Wacky Widget Organization Management System against its requirements. The test automation framework provides:

- **Complete black-box testing** - No dependency on implementation code
- **Subprocess-based execution** - Interacts with `main.py` via command-line interface only
- **Comprehensive coverage** - 150 automated test cases covering all functional areas
- **Bug detection focus** - Specific tests designed to uncover common edge cases and defects

### 6.2 Test Automation Architecture

#### 6.2.1 Framework Design
The automated testing framework (`run_blackbox_tests.py`) implements:

- **BlackBoxTester Class:** Main test harness that manages test execution
  - Runs `main.py` as a subprocess
  - Sends commands via stdin
  - Captures output from stdout/stderr
  - Validates expected outputs against actual results
  - Tracks pass/fail statistics

- **Test Isolation:** Each test case runs the application independently
  - Fresh instance per test prevents state contamination
  - 5-second timeout prevents hanging
  - Exception handling for robustness

#### 6.2.2 Test Case Structure
Each test case includes:
- **Test ID:** Unique identifier (BBT001-BBT150)
- **Description:** Clear statement of what is being tested
- **Input Commands:** List of commands to send to the application
- **Expected Outputs:** Strings that should appear in the output
- **Validation Mode:** 
  - `should_contain_all=False` (default): At least one expected output must be present
  - `should_contain_all=True`: All expected outputs must be present

### 6.3 Test Coverage Breakdown

The automated test suite implements all test categories defined in Section 2.3, with specific test IDs for traceability:

| Category | Test IDs | Count | Focus Areas |
|----------|----------|-------|-------------|
| A: Initialization & Setup | BBT001-BBT003C | 6 | President name validation, initialization edge cases |
| B: HIRE Operations | BBT004-BBT013B | 13 | Capacity limits, duplicate detection, hierarchy rules |
| C: FIRE Operations | BBT014-BBT018 | 5 | Vacancy creation, hierarchy enforcement, president protection |
| D: QUIT Operations | BBT019-BBT021E | 8 | Voluntary departure, subordinate preservation, case sensitivity |
| E: LAYOFF Operations | BBT022-BBT024A | 4 | Placement algorithm, comparable openings |
| F: TRANSFER Operations | BBT025-BBT028 | 4 | Authorization, cross-hierarchy moves, capacity validation |
| G: PROMOTE Operations | BBT029-BBT034 | 6 | Single-level promotion, eligibility, vacancy requirements |
| H: DISPLAY Operations | BBT035-BBT037 | 3 | Hierarchy visualization, vacancy display rules |
| I: Edge Cases & Integration | BBT038-BBT068 | 31 | Complex workflows, operation combinations |
| J: Bug Detection Tests | BBT069-BBT150 | 70 | Known defect patterns, edge cases |
| **Total** | | **150** | |

### 6.4 Execution and Reporting

#### 6.4.1 Running the Test Suite
```powershell
python run_blackbox_tests.py
```

#### 6.4.2 Test Output Format
For each test:
```
======================================================================
Running BBT001: Initialize president with valid name
======================================================================
Input commands: ['Alice', 'DISPLAY', 'EXIT']

Program output:
[actual program output]

[PASS] Expected: 'President: Alice' - FOUND

[PASS] BBT001 PASSED
```

#### 6.4.3 Summary Report
At completion:
```
======================================================================
TEST EXECUTION SUMMARY
======================================================================
Total Tests: 150
Passed: XX
Failed: XX
Pass Rate: XX.X%
======================================================================

FAILED TESTS:
  - BBT0XX: Description of failed test
  - ...
```

### 6.5 Defects Discovered Through Automation

The automated test suite is designed to detect the following defect categories:

1. **Subordinate Loss Defects (Critical)**
   - Tests BBT021A-C, BBT024A, BBT053-58, BBT091, BBT099, BBT116, BBT119-122
   - When manager is fired/quits/laid off, subordinates may disappear from display
   - Subordinates remain in data structures but become invisible/inaccessible

2. **Promotion System Defects (High)**
   - Tests BBT041-43, BBT043A, BBT098, BBT111-112
   - Unlimited promotions beyond VP
   - Creation of invalid hierarchies (VP under VP)
   - Capacity enforcement bypass through promotion

3. **Name Validation Defects (Medium)**
   - Tests BBT003A-C, BBT013A-B, BBT021D-E, BBT045, BBT047-48, BBT069, BBT081-89
   - Numeric names accepted when should be rejected
   - Names with spaces cause parsing errors
   - Case sensitivity inconsistencies
   - Special characters not properly validated

4. **Vacancy Display Defects (Medium)**
   - Tests BBT107, BBT120, BBT132, BBT142, BBT146
   - Vacancies at multiple levels display incorrectly
   - Deep hierarchy display stops at first vacancy
   - Nested vacancies cause display truncation

5. **Capacity Enforcement Defects (High)**
   - Tests BBT006, BBT008, BBT010, BBT028, BBT033, BBT113
   - Capacity limits may be bypassed through specific operation sequences
   - Promotion can create positions exceeding capacity

### 6.6 Test Data Implementation

The automated test suite implements the test data strategy defined in Section 2.4, using systematic combinations of organization sizes and name variations to achieve comprehensive coverage.

### 6.7 Continuous Testing Integration

#### 6.7.1 Test Suite Maintenance
- Add new test cases when bugs are discovered
- Update expected outputs if requirements change
- Group related tests for targeted execution
- Maintain test ID documentation

#### 6.7.2 Regression Testing
- Run full suite after any code changes
- Focus on previously failed test areas
- Verify bug fixes don't introduce new defects
- Track historical pass rates

### 6.8 Limitations and Future Enhancements

#### Current Limitations
- No performance/load testing
- Limited concurrency testing
- Output validation is string-based (may miss formatting issues)
- Timeout set to 5 seconds (may be too short for complex operations)

#### Potential Enhancements
- Parameterized test generation for combinatorial coverage
- Output parsing for structured validation
- Code coverage measurement integration
- Automated defect report generation
- Integration with CI/CD pipeline
- Property-based testing for random operation sequences
- Visual hierarchy validation (indentation checking)

### 6.9 Benefits of Automation

1. **Repeatability:** Same tests execute consistently
2. **Speed:** 150 tests run in minutes vs. hours manually
3. **Coverage:** Comprehensive edge case testing impossible manually
4. **Regression Detection:** Quickly identify when fixes break other functionality
5. **Documentation:** Test cases serve as executable specifications
6. **Bug Discovery:** Systematic exploration finds defects missed in manual testing
7. **Confidence:** High test count provides statistical confidence in quality

### 6.10 Integration with Manual Testing

The automated test suite complements manual testing by:
- **Smoke Testing:** Quick verification before manual test sessions
- **Regression Testing:** Automated checks while testers focus on exploratory testing
- **Bug Reproduction:** Convert manually found bugs into automated tests
- **Coverage Gaps:** Automated tests handle tedious repetitive scenarios
- **Documentation:** Test cases provide examples for manual test design

---

## 7. SUMMARY

This test plan provides a comprehensive approach to validating the Wacky Widget Organization Management System through both manual and automated testing methods. The combination of systematic test design, automated execution of 150 test cases, and focused manual exploratory testing ensures thorough coverage of functional requirements and edge cases.

**Key Deliverables:**
- Test plan document (this document)
- Automated test suite (`run_blackbox_tests.py`) with 150 test cases
- Test execution results and metrics
- Bug reports with severity classification
- Quality assessment report

**Success Criteria:**
- All critical and high-priority defects identified and documented
- 90%+ test execution completion
- Comprehensive coverage of all HR operations
- Clear assessment of system readiness for deployment

---

# Test Cases

## Test Suite Overview

**Total Test Cases:** 148  
**Pass Rate:** 79.1% (117 passing, 31 failing)  
**Test Type:** Black Box (CLI Interface Testing)

### Test Categories:
- **Initialization Tests:** BBT001-BBT003C (6 tests)
- **HIRE Operation Tests:** BBT004-BBT013B (12 tests)
- **FIRE Operation Tests:** BBT014-BBT018 (5 tests)
- **QUIT Operation Tests:** BBT019-BBT021E (7 tests)
- **LAYOFF Operation Tests:** BBT022-BBT024A (4 tests)
- **TRANSFER Operation Tests:** BBT025-BBT028 (4 tests)
- **PROMOTE Operation Tests:** BBT029-BBT044 (16 tests)
- **Name Validation Tests:** BBT045-BBT048, BBT081-BBT089 (12 tests)
- **Hierarchy Display Tests:** BBT053-BBT058 (6 tests)
- **Comprehensive Workflow Tests:** BBT059-BBT080 (22 tests)
- **Advanced Bug Detection Tests:** BBT090-BBT150 (54 tests)

---

## CATEGORY A: INITIALIZATION TESTS (BBT001-BBT003C)

### BBT001: Initialize president with valid name
- **Objective:** Verify president can be initialized successfully
- **Input:** `Alice`, `DISPLAY`, `EXIT`
- **Expected:** President: Alice
- **Status:**  PASS
- **Priority:** HIGH

### BBT002: Reject name with spaces
- **Objective:** Verify name validation rejects spaces
- **Input:** `Bob Smith`, `EXIT`
- **Expected:** Error message about invalid name
- **Status:**  PASS
- **Priority:** HIGH

### BBT003: Reject empty name
- **Objective:** Verify empty names are rejected
- **Input:** `""`, `Alice`, `EXIT`
- **Expected:** Eventually accepts "Alice"
- **Status:**  FAIL
- **Priority:** MEDIUM

### BBT003A: BUG - Numeric names should be rejected
- **Objective:** Verify numeric-only names are rejected
- **Input:** `123`, `DISPLAY`, `EXIT`
- **Expected:** Error: Invalid name
- **Status:**  FAIL - System accepts numeric names
- **Priority:** HIGH

### BBT003B: Single character names accepted
- **Objective:** Verify single character name handling
- **Input:** `X`, `DISPLAY`, `EXIT`
- **Expected:** President: X
- **Status:**  PASS
- **Priority:** LOW

### BBT003C: BUG - Invalid president name doesn't reprompt
- **Objective:** Verify program handles multiple invalid inputs
- **Input:** `""`, `""`, `ValidName`, `EXIT`
- **Expected:** Eventually accepts ValidName
- **Status:**  FAIL
- **Priority:** MEDIUM

---

## CATEGORY B: HIRE OPERATION TESTS (BBT004-BBT013B)

### BBT004: President hires first VP
- **Objective:** Basic hire operation
- **Input:** `HIRE President1 VP1`, `DISPLAY`
- **Expected:** Vice President: VP1, Success message
- **Status:**  PASS
- **Priority:** HIGH

### BBT005: President hires two VPs (at capacity)
- **Objective:** Verify capacity limit (2 VPs max)
- **Input:** `HIRE President1 VP1`, `HIRE President1 VP2`
- **Expected:** Both VPs successfully hired
- **Status:**  PASS
- **Priority:** HIGH

### BBT006: President cannot hire third VP
- **Objective:** Verify capacity enforcement
- **Input:** Attempt to hire 3rd VP
- **Expected:** Error: maximum direct reports
- **Status:**  PASS
- **Priority:** HIGH

### BBT007: VP hires supervisors up to capacity (3)
- **Objective:** Verify VP capacity limit
- **Input:** VP hires 3 supervisors
- **Expected:** All 3 successfully hired
- **Status:**  PASS
- **Priority:** HIGH

### BBT008: VP cannot hire 4th supervisor
- **Objective:** Verify VP capacity enforcement
- **Input:** VP attempts 4th supervisor
- **Expected:** Error: maximum direct reports
- **Status:**  PASS
- **Priority:** HIGH

### BBT009: Supervisor hires workers up to capacity (5)
- **Objective:** Verify Supervisor capacity limit
- **Input:** Supervisor hires 5 workers
- **Expected:** All 5 successfully hired
- **Status:**  PASS
- **Priority:** HIGH

### BBT010: Supervisor cannot hire 6th worker
- **Objective:** Verify Supervisor capacity enforcement
- **Input:** Supervisor attempts 6th worker
- **Expected:** Error: maximum direct reports
- **Status:**  PASS
- **Priority:** HIGH

### BBT011: Worker cannot hire anyone
- **Objective:** Verify workers cannot hire
- **Input:** `HIRE W1 Intern`
- **Expected:** Error: worker cannot hire
- **Status:**  PASS
- **Priority:** HIGH

### BBT012: Cannot hire duplicate name
- **Objective:** Verify name uniqueness enforced
- **Input:** Hire same name twice
- **Expected:** Error: name already exists
- **Status:**  PASS
- **Priority:** HIGH

### BBT013: Cannot hire under non-existent manager
- **Objective:** Verify manager exists check
- **Input:** `HIRE GhostManager NewPerson`
- **Expected:** Error: manager does not exist
- **Status:**  PASS
- **Priority:** MEDIUM

### BBT013A: BUG - Can hire employees with numeric names
- **Objective:** Verify numeric employee names rejected
- **Input:** `HIRE President1 999`
- **Expected:** Error: Invalid name
- **Status:**  FAIL - System accepts numeric names
- **Priority:** HIGH

### BBT013B: BUG - Can hire employees with special characters
- **Objective:** Verify special characters rejected
- **Input:** `HIRE President1 Test@123`
- **Expected:** Error: Invalid name
- **Status:**  FAIL - System accepts special characters
- **Priority:** HIGH

---

## CATEGORY C: FIRE OPERATION TESTS (BBT014-BBT018)

### BBT014: Fire employee with no reports
- **Objective:** Basic fire operation
- **Input:** `FIRE President1 VP1`
- **Expected:** Removed, vacancy created
- **Status:**  PASS
- **Priority:** HIGH

### BBT015: Fire employee with reports creates vacancy
- **Objective:** Verify vacancy creation with subordinates
- **Input:** Fire VP with supervisor
- **Expected:** Vacancy shown, supervisor remains
- **Status:**  PASS
- **Priority:** HIGH

### BBT016: Cannot fire president
- **Objective:** Verify president protection
- **Input:** `FIRE President1 President1`
- **Expected:** Error: Cannot fire president
- **Status:**  PASS
- **Priority:** HIGH

### BBT017: Cannot fire outside hierarchy
- **Objective:** Verify hierarchy enforcement
- **Input:** VP2 tries to fire VP1's subordinate
- **Expected:** Error: not in hierarchy
- **Status:**  PASS
- **Priority:** HIGH

### BBT018: Cannot fire non-existent employee
- **Objective:** Validate employee exists
- **Input:** `FIRE President1 Ghost`
- **Expected:** Error: does not exist
- **Status:**  PASS
- **Priority:** MEDIUM

---

## CATEGORY D: QUIT OPERATION TESTS (BBT019-BBT021E)

### BBT019: Employee can quit
- **Objective:** Basic quit operation
- **Input:** `QUIT VP1`
- **Expected:** Removed, vacancy created
- **Status:**  PASS
- **Priority:** HIGH

### BBT020: President cannot quit
- **Objective:** Verify president cannot quit
- **Input:** `QUIT President1`
- **Expected:** Error: President cannot quit
- **Status:**  PASS
- **Priority:** HIGH

### BBT021: Cannot quit non-existent employee
- **Objective:** Validate employee exists
- **Input:** `QUIT Ghost`
- **Expected:** Error: does not exist
- **Status:**  PASS
- **Priority:** MEDIUM

### BBT021A: When employee quits, subordinates remain visible
- **Objective:** Verify subordinate preservation
- **Input:** VP quits with supervisor and worker
- **Expected:** Vacancy shown with subordinates
- **Status:**  PASS
- **Priority:** HIGH

### BBT021B: Subordinates of quitter still in lookup
- **Objective:** Verify subordinates accessible after quit
- **Input:** Quit VP, then fire their subordinate
- **Expected:** Subordinate found
- **Status:**  PASS
- **Priority:** MEDIUM

### BBT021C: Fire also preserves subordinates in display
- **Objective:** Verify fire creates proper vacancy
- **Input:** Fire VP with subordinates
- **Expected:** Vacancy with subordinates visible
- **Status:**  PASS
- **Priority:** HIGH

### BBT021D: BUG - Case insensitive duplicate detection
- **Objective:** Verify case-insensitive name checking
- **Input:** Hire "VP1" then "vp1"
- **Expected:** Error: already exists
- **Status:**  FAIL - System treats as different names
- **Priority:** MEDIUM

### BBT021E: BUG - Case sensitive names treated as different
- **Objective:** Verify case handling in names
- **Input:** Hire "Bob" then "bob"
- **Expected:** Error: duplicate
- **Status:**  FAIL - Both names accepted
- **Priority:** MEDIUM

---

## CATEGORY E: LAYOFF OPERATION TESTS (BBT022-BBT024A)

### BBT022: Layoff with no opening removes employee
- **Objective:** Verify removal when no positions available
- **Input:** Layoff VP when president full
- **Expected:** No openings found, removed
- **Status:**  PASS
- **Priority:** HIGH

### BBT023: Layoff worker moves to opening in same group
- **Objective:** Verify closest placement priority
- **Input:** Layoff worker with vacancy under same supervisor
- **Expected:** Worker moved to vacancy
- **Status:**  PASS
- **Priority:** HIGH

### BBT024: Cannot layoff president
- **Objective:** President protection
- **Input:** `LAYOFF President1 President1`
- **Expected:** Error: Cannot layoff president
- **Status:**  PASS
- **Priority:** MEDIUM

### BBT024A: Layoff preserves subordinates
- **Objective:** Verify subordinates remain after layoff
- **Input:** Layoff supervisor with workers
- **Expected:** Workers still visible
- **Status:**  PASS
- **Priority:** HIGH

---

## CATEGORY F: TRANSFER OPERATION TESTS (BBT025-BBT028)

### BBT025: President can transfer across VPs
- **Objective:** Valid cross-hierarchy transfer
- **Input:** Transfer supervisor from VP1 to VP2
- **Expected:** Successfully placed
- **Status:**  PASS
- **Priority:** HIGH

### BBT026: VP can transfer within own hierarchy
- **Objective:** VP transferring workers between supervisors
- **Input:** Transfer worker between supervisors under same VP
- **Expected:** Successfully placed
- **Status:**  PASS
- **Priority:** HIGH

### BBT027: Supervisor cannot transfer
- **Objective:** Verify only VP/President can transfer
- **Input:** Supervisor attempts transfer
- **Expected:** Error: no permission
- **Status:**  PASS
- **Priority:** HIGH

### BBT028: Cannot transfer to full position
- **Objective:** Verify capacity check
- **Input:** Transfer to manager at capacity
- **Expected:** Error: maximum direct reports
- **Status:**  PASS
- **Priority:** HIGH

---

## CATEGORY G: PROMOTE OPERATION TESTS (BBT029-BBT044)

### BBT029: Promote worker to supervisor (one level)
- **Objective:** Valid one-level promotion
- **Input:** `PROMOTE VP1 W1`
- **Expected:** W1 becomes Supervisor
- **Status:**  PASS
- **Priority:** HIGH

### BBT030: Promote supervisor to VP (one level)
- **Objective:** Supervisor to VP promotion
- **Input:** `PROMOTE President1 S1`
- **Expected:** S1 becomes VP
- **Status:**  PASS
- **Priority:** HIGH

### BBT031: Cannot promote worker to VP (two levels)
- **Objective:** Verify one-level rule
- **Input:** `PROMOTE President1 W1`
- **Expected:** Error: can only be one level
- **Status:**  PASS
- **Priority:** HIGH

### BBT032: Cannot promote VP further
- **Objective:** VP is max level
- **Input:** `PROMOTE President1 VP1`
- **Expected:** Error: cannot be promoted further
- **Status:**  PASS
- **Priority:** HIGH

### BBT033: Cannot promote without vacancy
- **Objective:** Verify vacancy requirement
- **Input:** Promote when receiving manager at capacity
- **Expected:** Error: maximum direct reports
- **Status:**  PASS
- **Priority:** HIGH

### BBT034: Worker/Supervisor cannot be receiving manager
- **Objective:** Verify only VP/President can receive promotions
- **Input:** `PROMOTE S1 W1`
- **Expected:** Error: cannot promote
- **Status:**  PASS
- **Priority:** MEDIUM

### BBT035-BBT044: Additional promotion edge cases
*(Tests covering unlimited promotions, capacity limits, proper role assignment)*
- **Status:** Mostly PASS, 2 FAIL (BBT042, BBT043 - invalid hierarchy creation)
- **Priority:** HIGH

---

## CATEGORY H: NAME VALIDATION TESTS (BBT045-BBT048, BBT081-BBT089)

### BBT045: President name with spaces rejected
- **Input:** `John Smith`
- **Expected:** Error: Invalid
- **Status:**  PASS
- **Priority:** HIGH

### BBT047: Multi-word names parsed incorrectly
- **Input:** `HIRE President1 Carol Davis`
- **Expected:** Fails or handles space
- **Status:**  PASS
- **Priority:** MEDIUM

### BBT048: Names with leading/trailing spaces
- **Input:** `HIRE President1  SpaceName `
- **Expected:** Error: Invalid
- **Status:**  FAIL
- **Priority:** MEDIUM

### BBT081-BBT089: Extended name validation
- **BBT081:** Only spaces -  FAIL
- **BBT082:** Tabs -  PASS
- **BBT083:** Newlines -  FAIL
- **BBT084:** Removed (duplicate)
- **BBT085:** Underscores -  FAIL
- **BBT086:** Hyphens -  FAIL
- **BBT087:** Very long name (100+ chars) -  PASS
- **BBT088:** Single character -  PASS
- **BBT089:** Command word as name -  PASS

---

## CATEGORY I: HIERARCHY DISPLAY TESTS (BBT053-BBT058)

### BBT053: Display hierarchy when VP fired
- **Objective:** Subordinates remain visible after VP removal
- **Input:** Fire VP with supervisors and workers
- **Expected:** All subordinates visible under vacancy
- **Status:**  FAIL - Subordinates disappear
- **Priority:** CRITICAL

### BBT054: Display hierarchy when VP quits
- **Objective:** Subordinates visible after quit
- **Input:** VP quits with subordinates
- **Expected:** Vacancy with subordinates
- **Status:**  FAIL - Subordinates disappear
- **Priority:** CRITICAL

### BBT055: Display when Supervisor fired
- **Objective:** Workers remain visible
- **Input:** Fire supervisor with workers
- **Expected:** Vacancy with workers
- **Status:**  FAIL - Workers disappear
- **Priority:** CRITICAL

### BBT056-BBT058: Additional display tests
- **BBT056:** Supervisor quits -  PASS
- **BBT057:** Layoff VP -  FAIL
- **BBT058:** Deep hierarchy -  FAIL

---

## CATEGORY J: COMPREHENSIVE WORKFLOW TESTS (BBT059-BBT080)

*Tests covering complex multi-operation scenarios, vacancy filling, cascading operations, maximum capacities, and edge cases*

**Summary:**
- Total: 22 tests
- Pass: 20
- Fail: 2 (BBT075, BBT080)
- **Key Failures:** Nested vacancies not displaying correctly

---

## CATEGORY K: ADVANCED BUG DETECTION TESTS (BBT090-BBT150)

### Highlights:

**BBT091:** Subordinates lost after cascading fires -  FAIL  
**BBT099:** Layoff with subordinates -  FAIL  
**BBT116:** Display stops at vacancy -  FAIL  
**BBT119:** Deep hierarchy with vacancy -  FAIL  
**BBT130:** Layoff under vacancy -  FAIL  
**BBT132:** Multiple vacancies -  FAIL  
**BBT133:** SQL injection attempt -  FAIL  
**BBT134:** Escape sequences -  FAIL  
**BBT147:** Hire after quit preserves structure -  FAIL  
**BBT150:** Maximum nesting -  FAIL  

**Remaining tests (BBT090-BBT149):** Mostly  PASS

---

## DETAILED TEST CASE SPECIFICATIONS

### TC001: Initialize President with Valid Name
- **Objective:** Verify president can be initialized successfully
- **Preconditions:** Empty organization
- **Test Data:** Name = "Bob"
- **Steps:** 
  1. Start program
  2. Enter "Bob" as president name
- **Expected Result:** Success message, president created
- **Priority:** HIGH

### TC002: Initialize President with Name Containing Space
- **Objective:** Verify name validation rejects spaces
- **Preconditions:** Empty organization
- **Test Data:** Name = "Bob Smith"
- **Steps:** Enter "Bob Smith" as president name
- **Expected Result:** Error message about invalid name
- **Priority:** HIGH

### TC003: Initialize President with Empty String
- **Objective:** Verify empty names are rejected
- **Preconditions:** Empty organization
- **Test Data:** Name = ""
- **Steps:** Enter empty string
- **Expected Result:** Error message
- **Priority:** MEDIUM

### TC004: Initialize Second President
- **Objective:** Verify only one president allowed
- **Preconditions:** President already exists
- **Test Data:** Name = "Carol"
- **Steps:** Attempt to initialize second president
- **Expected Result:** Should not allow/error (implementation dependent)
- **Priority:** MEDIUM

### TC005: Display Empty Organization (President Only)
- **Objective:** Verify display with only president
- **Preconditions:** President initialized, no other employees
- **Steps:** Execute DISPLAY command
- **Expected Result:** Shows only "President: Bob"
- **Priority:** MEDIUM

### TC006: Invalid Command Syntax
- **Objective:** Verify unknown commands are handled
- **Preconditions:** President initialized
- **Test Data:** Command = "INVALID"
- **Steps:** Enter "INVALID"
- **Expected Result:** Error message about unknown command
- **Priority:** LOW

### TC007: Command with Extra Arguments
- **Objective:** Verify argument count validation
- **Preconditions:** President initialized
- **Test Data:** "DISPLAY extra arguments"
- **Steps:** Enter command with extra args
- **Expected Result:** Error about incorrect argument count
- **Priority:** MEDIUM

### TC008: Command with Missing Arguments
- **Objective:** Verify required arguments enforced
- **Preconditions:** President initialized
- **Test Data:** "HIRE Bob" (missing employee name)
- **Steps:** Enter incomplete command
- **Expected Result:** Error about incorrect argument count
- **Priority:** MEDIUM

### TC009: Case Sensitivity of Commands
- **Objective:** Verify commands work in different cases
- **Preconditions:** President initialized
- **Test Data:** "hire", "Hire", "HIRE"
- **Steps:** Try commands in various cases
- **Expected Result:** Should work (commands converted to uppercase)
- **Priority:** LOW

### TC010: EXIT Command
- **Objective:** Verify clean program exit
- **Preconditions:** Any state
- **Steps:** Enter "EXIT"
- **Expected Result:** Program exits gracefully
- **Priority:** LOW

---

## SUMMARY OF KNOWN BUGS

### Critical Bugs (Must Fix):
1. **Hierarchy Display Bug** - Subordinates disappear when manager is fired/quit/laid off
2. **Name Validation** - Accepts spaces, numbers, and special characters
3. **Case Sensitivity** - Names not compared case-insensitively

### High Priority Bugs:
4. **Invalid Hierarchy Creation** - VP can be promoted to create VP under VP
5. **Nested Vacancy Display** - Deep hierarchies don't show properly with vacancies

### Medium Priority Bugs:
6. **Special Character Handling** - SQL injection, escape sequences not validated
7. **Multiple Vacancies** - Not all vacancies display at same level

---

## Test Execution Statistics

**Total Tests:** 148  
**Passed:** 117 (79.1%)  
**Failed:** 31 (20.9%)

### By Category:
- **Initialization:** 4/6 pass (66.7%)
- **HIRE:** 10/12 pass (83.3%)
- **FIRE:** 5/5 pass (100%)
- **QUIT:** 5/7 pass (71.4%)
- **LAYOFF:** 4/4 pass (100%)
- **TRANSFER:** 4/4 pass (100%)
- **PROMOTE:** 14/16 pass (87.5%)
- **Name Validation:** 6/12 pass (50%)
- **Hierarchy Display:** 1/6 pass (16.7%)
- **Workflows:** 20/22 pass (90.9%)
- **Advanced:** 44/54 pass (81.5%)

---

# Test Results

## 1. Introduction

**Purpose of Testing:**  
The black box tests aim to verify that the Wacky Widget Organization program meets functional requirements, particularly regarding initialization, employee management, hierarchy rules, input validation, and display of organizational structure.

**Scope:**  
- Tested via CLI only, without importing program code.  
- Focused on Initialization, Hire, Fire, Quit, Promote, Layoff, and Display modules.  
- Excludes performance testing, GUI testing, and integration with external systems.

**Methodology:**  
- Automated black box tests run through `main.py`.  
- Each test provides input commands and checks output for expected results.  
- Tests run independently, no multiple passes required.  

## 2. Test Summary

- **Total Tests:** 148
- **Passed:** 117
- **Failed:** 31
- **Pass Rate:** 79.1%

**Module Coverage**
- Initialization: 6 tests
- Hire: 12 tests
- Fire: 5 tests
- Quit: 7 tests
- Layoff: 4 tests
- Transfer: 4 tests
- Promotion: 16 tests
- Name Validation: 12 tests
- Hierarchy Display: 6 tests
- Comprehensive Workflow: 22 tests
- Advanced Bug Detection Tests: 54 tests

## 3. Detailed Test Results

**Initialization Module**
| Test ID | Description | Result | Priority | Bug ID | Spec Bug |
|---------|-------------|--------|----------|--------|----------|
| BBT001 | Initialize president with valid name |  Pass | High | — | — |
| BBT002 | Reject name with spaces |  Pass | High | — | — |
| BBT003 | Reject empty name |  Fail | Medium | BUG-009 | SPEC-010 |
| BBT003A | Numeric names should be rejected |  Fail | High | BUG-002 | SPEC-006 |
| BBT003B | Single character names accepted |  Pass | Low | — | — |
| BBT003C | Invalid name does not reprompt |  Fail | Medium | BUG-010 | SPEC-010 |

**Hire Module**
| Test ID  | Description                                   | Result     | Priority | Bug ID | Spec Bug |
|----------|-----------------------------------------------|------------|----------|--------|----------|
| BBT004   | President hires first VP                      |  Pass    | High     | —      | — |
| BBT005   | President hires two VPs (at capacity)         |  Pass    | High     | —      | — |
| BBT006   | President cannot hire third VP                |  Pass    | High     | —      | — |
| BBT007   | VP hires supervisors up to capacity (3)       |  Pass    | High     | —      | — |
| BBT008   | VP cannot hire 4th supervisor                 |  Pass    | High     | —      | — |
| BBT009   | Supervisor hires workers up to capacity (5)   |  Pass    | High     | —      | — |
| BBT010   | Supervisor cannot hire 6th worker             |  Pass    | High     | —      | — |
| BBT011   | Worker cannot hire anyone                     |  Pass    | High     | —      | — |
| BBT012   | Cannot hire duplicate name                    |  Pass    | High     | —      | — |
| BBT013   | Cannot hire under non-existent manager        |  Pass    | Medium   | —      | — |
| BBT013A  | Numeric names accepted incorrectly            |  Fail    | High     | BUG-003 | SPEC-006 |
| BBT013B  | Special characters accepted incorrectly       |  Fail    | High     | BUG-004 | SPEC-006 |

**Fire Module**
| Test ID | Description | Result | Priority | Bug ID | Spec Bug |
|---------|-------------|--------|----------|--------|----------|
| BBT014 | Fire employee with no reports |  Pass | High | — | — |
| BBT015 | Fire employee with reports |  Pass | High | — | — |
| BBT016 | Cannot fire president |  Pass | High | — | — |
| BBT017 | Cannot fire outside hierarchy |  Pass | High | — | — |
| BBT018 | Cannot fire non-existent employee |  Pass | Medium | — | — |

**Quit Module**
| Test ID | Description | Result | Priority | Bug ID | Spec Bug |
|---------|-------------|--------|----------|--------|----------|
| BBT019 | Employee can quit |  Pass | High | — | — |
| BBT020 | President cannot quit |  Pass | High | — | — |
| BBT021 | Cannot quit non-existent employee |  Fail | Medium | — | SPEC-010 |
| BBT021A | Subordinates remain visible after quit |  Pass | High | — | — |
| BBT021B | Subordinates remain accessible after quit |  Pass | Medium | — | — |
| BBT021C | Fire preserves subordinates |  Pass | High | — | — |
| BBT021D | Case-insensitive duplicates missed |  Fail | Medium | BUG-005 | SPEC-006 |
| BBT021E | Case-sensitive duplicates treated separately |  Fail | Medium | BUG-005 | SPEC-006 |

**Layoff Module**
| Test ID | Description | Result | Priority | Bug ID | Spec Bug |
|---------|-------------|--------|----------|--------|----------|
| BBT022 | Layoff with no opening |  Pass | High | — | — |
| BBT023 | Worker moved to local vacancy |  Pass | High | — | — |
| BBT024 | Cannot layoff president |  Pass | Medium | — | — |
| BBT024A | Layoff preserves subordinates |  Pass | High | — | — |

**Transfer Module**
| Test ID | Description | Result | Priority | Bug ID | Spec Bug |
|---------|-------------|--------|----------|--------|----------|
| BBT025 | President transfers across VPs |  Pass | High | — | — |
| BBT026 | VP transfers within own hierarchy |  Pass | High | — | — |
| BBT027 | Supervisor cannot transfer |  Pass | High | — | — |
| BBT028 | Cannot transfer to full position |  Fail | High | — | SPEC-004 |

**Promotion Module**
| Test ID | Description | Result | Priority | Bug ID | Spec Bug |
|---------|-------------|--------|----------|--------|----------|
| BBT029 | Promote worker to supervisor |  Pass | High | — | — |
| BBT030 | Promote supervisor to VP |  Pass | High | — | — |
| BBT031 | Cannot promote worker to VP |  Fail | High | — | SPEC-002 |
| BBT032 | VP cannot be promoted |  Pass | High | — | — |
| BBT033 | Cannot promote without vacancy |  Fail | High | — | SPEC-009 |
| BBT034 | Worker/Supervisor cannot be receiving manager |  Pass | Medium | — | — |
| BBT035–BBT044 | Advanced promotion edge cases | Mixed | High | BUG-007, BUG-008 | SPEC-002 |

**Name Validation Module**
| Test ID | Description | Result | Priority | Bug ID | Spec Bug |
|---------|-------------|--------|----------|--------|----------|
| BBT045 | President name with spaces rejected |  Pass | High | — | — |
| BBT047 | Multi-word names parsed incorrectly |  Pass | Medium | — | — |
| BBT048 | Leading/trailing spaces allowed |  Fail | Medium | BUG-006 | SPEC-006 |
| BBT081 | Only spaces |  Fail | Medium | BUG-017 | SPEC-006 |
| BBT082 | Tabs in names |  Pass | Medium | — | — |
| BBT083 | Newlines |  Fail | Medium | BUG-018 | SPEC-006 |
| BBT084 | Duplicate test (removed) | — | — | — | — |
| BBT085 | Underscores |  Fail | Medium | BUG-019 | SPEC-006 |
| BBT086 | Hyphens |  Fail | Medium | BUG-020 | SPEC-006 |
| BBT087 | Very long name (100+ chars) |  Pass | Medium | — | — |
| BBT088 | Single character allowed |  Pass | Low | — | — |
| BBT089 | Command word used as name |  Pass | Low | — | — |

**Display Module**
| Test ID | Description | Result | Priority | Bug ID | Spec Bug |
|---------|-------------|--------|----------|--------|----------|
| BBT053 | Display after VP fired |  Fail | **Critical** | BUG-001 | SPEC-001, SPEC-008 |
| BBT054 | Display after VP quits |  Fail | **Critical** | BUG-030 | SPEC-001, SPEC-008 |
| BBT055 | Display after supervisor fired |  Fail | **Critical** | BUG-029 | SPEC-001, SPEC-008 |
| BBT056 | Supervisor quits |  Pass | High | — | — |
| BBT057 | Layoff VP |  Fail | High | BUG-027 | SPEC-001, SPEC-008 |
| BBT058 | Deep hierarchy display |  Fail | High | BUG-028 | SPEC-001, SPEC-008 |

**Advanced Bug Tests**
| Test ID | Issue Detected | Result | Priority | Bug ID | Spec Bug |
|---------|----------------|--------|----------|--------|----------|
| BBT091 | Subordinates lost after cascading fires |  Fail | Critical | BUG-011 | SPEC-001, SPEC-008 |
| BBT099 | Layoff removes subordinates incorrectly |  Fail | High | BUG-012 | SPEC-003, SPEC-008 |
| BBT116 | Display stops at vacancy |  Fail | Critical | BUG-013 | SPEC-001, SPEC-008 |
| BBT119 | Deep hierarchy with vacancy breaks |  Fail | High | BUG-014 | SPEC-001, SPEC-008 |
| BBT130 | Layoff under vacancy collapses structure |  Fail | High | BUG-021, BUG-031 | SPEC-003, SPEC-005 |
| BBT132 | Multiple vacancies break display |  Fail | High | BUG-015 | SPEC-001, SPEC-007 |
| BBT133 | SQL injection attempt in names |  Fail | High | BUG-022 | SPEC-006 |
| BBT134 | Escape sequences allowed |  Fail | Medium | BUG-023 | SPEC-006 |
| BBT147 | Hire after quit corrupts structure |  Fail | High | BUG-024 | SPEC-005 |
| BBT150 | Maximum nesting level |  Fail | High | BUG-025 | SPEC-001, SPEC-008 |

## 4. Specification Bugs

In addition to implementation bugs, the requirements specification itself contains several critical ambiguities, contradictions, and omissions that contributed to implementation errors and testing difficulties:

**SPEC-001: Contradictory Display Rules for Vacancies (Requirement 11b)**  
The specification states: "Do not display vacancies for worker vacancies, or for supervisors at any level if the entire organization below is also vacant." This creates a logical contradiction:
- Worker vacancies should not be displayed
- But supervisor vacancies should only be hidden "if the entire organization below is also vacant"
- How can the system determine if the organization below is vacant without tracking worker vacancies?
- **Impact:** Ambiguous implementation leading to display bugs (BUG-001, BUG-013, BUG-026)

**SPEC-002: Undefined "Different Organization" for Promotions (Requirement 8d)**  
The rule states: "A promotion must be to a different organization. This means that as a result of a promotion, the new manager may not supervise his or her former peers."
- What constitutes a "different organization"? Different VP hierarchy? Different department?
- The second sentence doesn't logically follow from the first
- If promoted, they're no longer peers with former colleagues, making "former peers" restriction unclear
- **Impact:** Allows invalid VP→VP hierarchies (BUG-007, BUG-008)

**SPEC-003: Missing Definition of "Comparable Opening" (Requirement 6b-c)**  
Layoff rules reference "comparable opening" and "closest possible move" without defining:
- What makes an opening "comparable"? Same role level only?
- Can a Supervisor be laid off to a Supervisor position under a different VP?
- The preference order is given but "comparable" lacks explicit definition
- **Impact:** Ambiguous layoff placement logic, implementation inconsistencies

**SPEC-004: Ambiguous "Same Level" for Transfers (Requirement 7b)**  
"Transfers are to the same level" lacks clarity:
- Does "same level" mean hierarchical tier (Worker/Supervisor/VP) or specific position in reporting chain?
- Is Worker under Supervisor A at the same level as Worker under Supervisor B?
- No specification of whether level means role type or organizational depth
- **Impact:** Transfer validation logic unclear

**SPEC-005: Incomplete Firing Rules for Vacancies (Requirement 4)**  
Firing requirement mentions people "sometimes report to a vacant position" but doesn't specify:
- What happens when firing someone who reports to a vacancy?
- Can a vacancy be fired?
- How do vacancies propagate through multiple hierarchical levels?
- **Impact:** Undefined behavior for nested vacancies (BUG-026, BUG-130)

**SPEC-006: Missing Name Format Specification (Requirement 2a)**  
Critical validation rules left undefined: "It isn't specified whether the names are just first names, or first names and last names. It's up to you to decide."
- No guidance on valid characters (letters, numbers, special chars)
- No guidance on spaces, length limits, or formatting
- No specification of case sensitivity for uniqueness checks
- **Impact:** Weak input validation allowing numeric names, special characters, SQL injection attempts (BUG-002, BUG-003, BUG-004, BUG-022)

**SPEC-007: Contradictory Vacancy Display with Empty Organization**  
Requirement 11b states: "if everybody except the president leaves, the organization chart will show just the president"
- But earlier it says to show supervisory position vacancies
- If all VPs quit, shouldn't those VP vacancies be displayed?
- Contradicts the rule about showing supervisory vacancies
- **Impact:** Inconsistent vacancy display behavior

**SPEC-008: Undefined Nested Vacancy Behavior**  
Requirements never specify display/traversal when:
- A VP vacancy has a Supervisor with Workers beneath it
- Whether the entire chain through vacancy nodes should be visible
- How deep the display should recurse through vacancy objects
- **Impact:** Critical display bugs where subordinates disappear (BUG-001, BUG-013, BUG-028, BUG-030)

**SPEC-009: Promotion Vacancy Requirement Ambiguity (Requirement 8b)**  
"Of course, there must be a vacancy" doesn't specify:
- Must it be an explicit Vacancy object at the target level?
- Or just an open slot (unfilled position)?
- Difference between empty slot and Vacancy object unclear
- **Impact:** Confusion about when promotions are valid

**SPEC-010: Missing Error Handling and User Interaction Specifications**  
The requirements never specify:
- What error messages should be displayed for various failures
- Whether the system should reprompt on invalid input or fail once
- How to handle edge cases like duplicate names with different cases
- Expected behavior when sequential invalid inputs occur
- **Impact:** Inconsistent user experience, failed validation tests (BBT003, BBT003C, BBT021)

**Summary of Specification Issues:**  
These specification bugs demonstrate that many implementation defects stem from ambiguous, contradictory, or missing requirements. A revised SRS should clearly define:
1. Vacancy display and traversal rules at all levels
2. Precise definitions of "comparable," "same level," and "different organization"
3. Complete name validation rules with allowed character sets
4. Error handling and user interaction patterns
5. Behavior for edge cases involving nested vacancies

## 5. Bug Summary

A total of 30 defects (BUG-001 → BUG-030) were identified across the Wacky Widget Organization System. These span Display, Name Validation, Hire/Fire/Layoff Operations, Initialization, and Promotion Logic.

**Severity distribution:**
- **Critical:** 13 bugs
- **Major:** 8 bugs
- **Minor:** 9 bugs

The most serious issues involve loss of subordinate data, display corruption, invalid promotions, and unsafe name validation.

**Critical issues** affect core functionality such as display corruption, subordinate loss, invalid hierarchy formation, and unsafe input handling.  
**Major issues** include invalid name acceptance, improper handling of hires and layoffs, and display failures under complex structures.  
**Minor issues** relate to whitespace handling, name formatting, and multi-vacancy display edge cases.

### Critical Bugs
- **BUG-001:** Subordinates disappear after FIRE
- **BUG-007:** VP can promote Supervisor into invalid VP → VP hierarchy
- **BUG-008:** Unlimited promotions break hierarchy rules
- **BUG-011:** Cascading fires delete entire subtree
- **BUG-012:** Layoff operation deletes subordinates
- **BUG-013:** Display stops recursing at vacancy
- **BUG-022:** SQL injection attempt accepted
- **BUG-026:** Nested vacancy display completely broken
- **BUG-027:** Layoff VP → all subordinates gone
- **BUG-028:** Deep hierarchy collapses after FIRE
- **BUG-029:** Supervisor FIRE loses workers
- **BUG-030:** VP quit loses subordinate visibility

## 6. Observations

- **Display Issues:** Multiple critical bugs (BUG-001, BUG-030, BUG-026) show that the display loop does not recurse correctly through vacancies and subordinates. Recommend immediate fix before release.  
- **Input Validation:** System currently allows numeric-only names, special characters, and whitespace-only names (BUG-002, BUG-003, BUG-017). Input sanitization should be strengthened.  
- **Hierarchy Rules:** Promotion logic allows creation of invalid VP hierarchy (BUG-007, BUG-008). Level validation needed in promote employee functionality.
- **Specification Issues:** Many implementation bugs trace back to ambiguous or contradictory requirements (see Section 4). A significant portion of defects could have been prevented with clearer SRS documentation.
- **Overall:** While basic hire/fire functionality works, critical bugs in display, input validation, and hierarchy may confuse users and violate SRS requirements.  

## 7. Final Assessment of Quality

Overall, the Wacky Widget Organization system demonstrates partial compliance with the expected functional requirements. While core features such as basic hiring, firing, quitting, and simple promotions work under normal conditions, the system exhibits significant quality issues when exposed to edge cases, invalid input, vacancy propagation, and deeper hierarchical operations.

### Strengths
- Basic CRUD operations (hire/fire/quit) work reliably in standard scenarios.
- The system accepts a wide range of commands consistently.
- Most simple hierarchical transitions behave as expected.

### Major Quality Concerns
- **Hierarchy Corruption:** Several operations (fire, quit, layoff) cause subtrees to disappear or collapse.
- **Display Instability:** The display function fails to traverse all levels, breaks on vacancies, and loses subordinates.
- **Weak Input Validation:** Numeric names, special characters, SQL-injection-like input, whitespace-only names, and escape sequences are accepted.
- **Promotion Rule Violations:** Promotions can create invalid hierarchies or skip levels.
- **Inconsistent Vacancy Handling:** Vacancies can break traversal, corrupt display, or incorrectly delete subordinates.

### Release Readiness

In its current state, the system is **not ready for production or classroom demo use**, particularly due to issues that compromise:
- Correctness of displayed information
- Structural integrity of the hierarchy
- Safety and validity of user input

**Recommendation:** Address all critical bugs (BUG-001, BUG-007, BUG-008, BUG-011, BUG-012, BUG-013, BUG-022, BUG-026, BUG-027, BUG-028, BUG-029, BUG-030) before any production deployment or demonstration.

---

**Document End**  
**Last Updated:** November 20, 2025  
**Test Framework:** run_blackbox_tests.py  
**Testing Method:** Black Box CLI Interface Testing
