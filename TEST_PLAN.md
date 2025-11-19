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

### 6.3 Test Coverage Areas

#### Category A: Initialization & Setup (BBT001-BBT003C) - 6 tests
- Valid president name initialization
- Name validation (spaces, empty, numeric, single character)
- Invalid name reprompting behavior

#### Category B: HIRE Operations (BBT004-BBT013B) - 13 tests
- Hiring at all organizational levels
- Capacity enforcement (President: 2, VP: 3, Supervisor: 5)
- Worker hiring restrictions
- Duplicate name detection
- Invalid manager validation
- Name format validation (numeric, special characters)

#### Category C: FIRE Operations (BBT014-BBT018) - 5 tests
- Firing employees with and without reports
- Vacancy creation on fire
- President protection (cannot be fired)
- Hierarchy enforcement
- Non-existent employee handling

#### Category D: QUIT Operations (BBT019-BBT021E) - 8 tests
- Voluntary departure functionality
- President quit restriction
- Subordinate preservation after quit
- Case sensitivity in names
- Display behavior after quit

#### Category E: LAYOFF Operations (BBT022-BBT024A) - 4 tests
- Layoff with no comparable openings
- Placement in available positions
- President layoff restriction
- Subordinate handling during layoff

#### Category F: TRANSFER Operations (BBT025-BBT028) - 4 tests
- President and VP transfer authorization
- Cross-hierarchy transfers
- Supervisor transfer restrictions
- Capacity validation

#### Category G: PROMOTE Operations (BBT029-BBT034) - 6 tests
- Single-level promotions (Worker→Supervisor, Supervisor→VP)
- Multi-level promotion prevention
- VP promotion limit
- Vacancy requirement
- Receiving manager eligibility

#### Category H: DISPLAY Operations (BBT035-BBT037) - 3 tests
- Complete hierarchy visualization
- Supervisory vacancy display
- Worker vacancy handling

#### Category I: Edge Cases & Integration (BBT038-BBT068) - 31 tests
- Vacancy filling scenarios
- Complex multi-operation workflows
- Case sensitivity verification
- Maximum capacity scenarios
- Promoted employee capacity changes
- Transfer and promote combinations
- Deep hierarchy operations

#### Category J: Bug Detection Tests (BBT069-BBT150) - 82 tests
Targeted tests for known defect patterns:
- **Subordinate Visibility:** Tests for subordinates disappearing after manager removal
- **Promotion Defects:** Unlimited promotions, invalid hierarchy creation, capacity bypass
- **Name Validation:** Spaces, special characters, case sensitivity, SQL injection
- **Hierarchy Integrity:** Circular reporting, nested VPs, vacancy propagation
- **Operation Combinations:** Quit/fire/layoff then rehire, multiple cascading operations
- **Vacancy Management:** Multiple vacancies, filling specific vacancies, operations under vacancies
- **Capacity Enforcement:** Promotion exceeding limits, transfer to full positions
- **Display Issues:** Vacancy display depth, nested vacancies, empty organization

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

### 6.6 Test Data Strategy

#### 6.6.1 Organization Sizes
- **Minimal:** President only (initialization tests)
- **Small:** 1-2 VPs with sparse reporting structure
- **Medium:** Multiple VPs with several supervisors
- **Full:** All positions at maximum capacity
- **Deep:** Maximum nesting depth with vacancies

#### 6.6.2 Name Variations
- Valid alphabetic names (Alice, Bob, President1)
- Single character (X)
- All capitals (PRESIDENT)
- All lowercase (president)
- Mixed case (AlIcE)
- Numeric (123, 999)
- Special characters (@, #, -, _)
- Spaces (John Smith, leading/trailing spaces)
- Very long names (100+ characters)
- Command words (EXIT, HIRE)
- Escape sequences (\n, \t)
- SQL injection attempts

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



