# Test Cases: Wacky Widget Organization Management System

**Project:** Wacky Widget Organization Management System  
**Date:** November 18, 2025  
**Test Team:** Team 2 - Black Box Testing

---

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

**Last Updated:** November 20, 2025  
**Test Framework:** run_blackbox_tests.py  
**Testing Method:** Black Box CLI Interface Testing

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

## CATEGORY B: HIRE OPERATIONS (TC011-TC025)

### TC011: President Hires First VP
- **Objective:** Basic hire operation
- **Preconditions:** President exists, no VPs
- **Test Data:** HIRE Bob Alice
- **Steps:** Execute "HIRE Bob Alice"
- **Expected Result:** Success message, Alice hired as VP under Bob
- **Priority:** HIGH

### TC012: President Hires Second VP (At Capacity)
- **Objective:** Verify capacity limit (2 VPs max)
- **Preconditions:** President has 1 VP
- **Steps:** Hire second VP
- **Expected Result:** Success, both VPs exist
- **Priority:** HIGH

### TC013: President Hires Third VP (Over Capacity)
- **Objective:** Verify capacity enforcement
- **Preconditions:** President has 2 VPs
- **Steps:** Attempt to hire third VP
- **Expected Result:** Error: maximum direct reports reached
- **Priority:** HIGH

### TC014: VP Hires First Supervisor
- **Objective:** Verify VP can hire
- **Preconditions:** VP exists
- **Steps:** HIRE Alice Carol
- **Expected Result:** Success, Carol hired as Supervisor under Alice
- **Priority:** HIGH

### TC015: VP Hires at Capacity (3 Supervisors)
- **Objective:** Verify VP capacity limit
- **Preconditions:** VP has 2 supervisors
- **Steps:** Hire third supervisor
- **Expected Result:** Success
- **Priority:** MEDIUM

### TC016: VP Exceeds Capacity (4 Supervisors)
- **Objective:** Verify VP capacity enforcement
- **Preconditions:** VP has 3 supervisors
- **Steps:** Attempt fourth hire
- **Expected Result:** Error: maximum direct reports reached
- **Priority:** HIGH

### TC017: Supervisor Hires Workers Up to Capacity (5)
- **Objective:** Verify Supervisor capacity limit
- **Preconditions:** Supervisor exists
- **Steps:** Hire 5 workers sequentially
- **Expected Result:** All 5 succeed
- **Priority:** HIGH

### TC018: Supervisor Exceeds Capacity (6 Workers)
- **Objective:** Verify Supervisor capacity enforcement
- **Preconditions:** Supervisor has 5 workers
- **Steps:** Attempt sixth hire
- **Expected Result:** Error: maximum direct reports reached
- **Priority:** HIGH

### TC019: Worker Attempts to Hire
- **Objective:** Verify workers cannot hire
- **Preconditions:** Worker exists
- **Steps:** HIRE WorkerName NewName
- **Expected Result:** Error: worker cannot hire
- **Priority:** HIGH

### TC020: Hire with Duplicate Name
- **Objective:** Verify name uniqueness enforced
- **Preconditions:** Employee "Alice" exists
- **Steps:** Attempt to hire another "Alice"
- **Expected Result:** Error: name already exists
- **Priority:** HIGH

### TC021: Hire with Non-Existent Manager
- **Objective:** Verify manager exists check
- **Preconditions:** Normal organization
- **Test Data:** HIRE GhostManager NewName
- **Steps:** Reference non-existent manager
- **Expected Result:** Error: manager does not exist
- **Priority:** MEDIUM

### TC022: Hire Fills Vacancy After Fire
- **Objective:** Verify vacancy filling
- **Preconditions:** VP position vacant
- **Steps:** 
  1. President had 2 VPs
  2. One VP fired (vacancy created)
  3. Hire new VP
- **Expected Result:** New VP fills vacancy, capacity = 2
- **Priority:** HIGH

### TC023: Hire with Special Characters in Name
- **Objective:** Verify name validation with special chars
- **Test Data:** Names with @, #, $, etc.
- **Steps:** Attempt hire with special characters
- **Expected Result:** Should reject or accept consistently
- **Priority:** LOW

### TC024: Hire with Very Long Name
- **Objective:** Verify name length handling
- **Test Data:** 100+ character name
- **Steps:** Attempt hire
- **Expected Result:** Should handle gracefully
- **Priority:** LOW

### TC025: Hire into Vacant Position That Has Reports
- **Objective:** Verify vacancy with subordinates handling
- **Preconditions:** VP fired, but had supervisors reporting
- **Steps:** Hire new VP
- **Expected Result:** New VP inherits the supervisors
- **Priority:** HIGH

---

## CATEGORY C: FIRE OPERATIONS (TC026-TC035)

### TC026: President Fires Direct VP
- **Objective:** Basic fire operation
- **Preconditions:** President has VP with no reports
- **Steps:** FIRE Bob Alice
- **Expected Result:** Alice removed, vacancy remains
- **Priority:** HIGH

### TC027: Fire Employee with No Reports
- **Objective:** Verify simple removal
- **Preconditions:** Worker exists with no reports
- **Steps:** Fire worker
- **Expected Result:** Worker removed, no vacancy shown
- **Priority:** MEDIUM

### TC028: Fire Employee with Reports
- **Objective:** Verify vacancy creation with subordinates
- **Preconditions:** VP has supervisors
- **Steps:** Fire VP
- **Expected Result:** VP removed, vacancy created, supervisors report to vacancy
- **Priority:** HIGH

### TC029: Attempt to Fire President
- **Objective:** Verify president cannot be fired
- **Preconditions:** President exists
- **Steps:** FIRE Bob Bob
- **Expected Result:** Error: cannot fire president
- **Priority:** HIGH

### TC030: Fire Outside Hierarchy
- **Objective:** Verify hierarchy enforcement
- **Preconditions:** VP1 and VP2 exist as peers, VP1 has Supervisor
- **Steps:** VP2 attempts to fire VP1's supervisor
- **Expected Result:** Error: not in hierarchy
- **Priority:** HIGH

### TC031: Fire with Non-Existent Manager
- **Objective:** Validate manager exists
- **Steps:** FIRE GhostManager Alice
- **Expected Result:** Error: manager does not exist
- **Priority:** MEDIUM

### TC032: Fire with Non-Existent Employee
- **Objective:** Validate employee exists
- **Steps:** FIRE Bob GhostEmployee
- **Expected Result:** Error: employee does not exist
- **Priority:** MEDIUM

### TC033: Fire from Bottom of Hierarchy (Worker)
- **Objective:** Verify leaf node removal
- **Preconditions:** Complete hierarchy to worker
- **Steps:** Supervisor fires worker
- **Expected Result:** Worker removed completely
- **Priority:** MEDIUM

### TC034: Fire Creates Vacancy Visible in Display
- **Objective:** Verify vacancy display
- **Preconditions:** VP with reports
- **Steps:** 
  1. Fire VP
  2. Execute DISPLAY
- **Expected Result:** Shows "VACANCY: Vice President" with reports beneath
- **Priority:** MEDIUM

### TC035: Multiple Fires in Same Branch
- **Objective:** Test consecutive removals
- **Preconditions:** VP with 3 supervisors
- **Steps:** Fire all 3 supervisors
- **Expected Result:** 3 vacancies or appropriate cleanup
- **Priority:** MEDIUM

---

## CATEGORY D: QUIT OPERATIONS (TC036-TC042)

### TC036: Worker Quits
- **Objective:** Basic quit operation
- **Preconditions:** Worker exists
- **Steps:** QUIT WorkerName
- **Expected Result:** Worker removed
- **Priority:** HIGH

### TC037: Supervisor Quits with No Reports
- **Objective:** Quit with no subordinates
- **Preconditions:** Supervisor with no workers
- **Steps:** QUIT SupervisorName
- **Expected Result:** Supervisor removed completely
- **Priority:** MEDIUM

### TC038: VP Quits with Reports
- **Objective:** Quit creates vacancy
- **Preconditions:** VP with supervisors
- **Steps:** QUIT VPName
- **Expected Result:** VP removed, vacancy created, supervisors remain
- **Priority:** HIGH

### TC039: President Attempts to Quit
- **Objective:** Verify president cannot quit
- **Preconditions:** President exists
- **Steps:** QUIT Bob
- **Expected Result:** Error: president cannot quit
- **Priority:** HIGH

### TC040: Quit Non-Existent Employee
- **Objective:** Validate employee exists
- **Steps:** QUIT GhostEmployee
- **Expected Result:** Error: employee does not exist
- **Priority:** MEDIUM

### TC041: Multiple Employees Quit Sequentially
- **Objective:** Test state consistency
- **Preconditions:** Multiple workers under supervisor
- **Steps:** Have 3 workers quit one by one
- **Expected Result:** All removed properly
- **Priority:** LOW

### TC042: Entire Branch Quits Except President
- **Objective:** Verify minimal organization display
- **Preconditions:** Full organization
- **Steps:** Everyone quits except president
- **Expected Result:** Display shows only president
- **Priority:** MEDIUM

---

## CATEGORY E: LAYOFF OPERATIONS (TC043-TC052)

### TC043: Layoff Worker - Opening in Same Supervisor Group
- **Objective:** Verify closest placement priority
- **Preconditions:** Supervisor1 has 5 workers, Supervisor1 lays off Worker1, Supervisor1 has vacancy
- **Steps:** LAYOFF Supervisor1 Worker1
- **Expected Result:** Worker1 moved to opening under same supervisor
- **Priority:** HIGH

### TC044: Layoff Worker - Opening in Same VP Group
- **Objective:** Second priority placement
- **Preconditions:** 
  - Supervisor1 full (5 workers)
  - Supervisor2 under same VP has opening
- **Steps:** LAYOFF Supervisor1 Worker1
- **Expected Result:** Worker1 moves to Supervisor2
- **Priority:** HIGH

### TC045: Layoff Worker - Opening in Different VP Group
- **Objective:** Third priority placement
- **Preconditions:**
  - All supervisors under VP1 full
  - Supervisor under VP2 has opening
- **Steps:** LAYOFF from VP1's supervisor
- **Expected Result:** Worker moves to VP2's supervisor
- **Priority:** HIGH

### TC046: Layoff Worker - No Comparable Opening
- **Objective:** Verify removal when no openings
- **Preconditions:** All worker positions full
- **Steps:** LAYOFF Supervisor Worker
- **Expected Result:** "No comparable openings found", worker removed
- **Priority:** HIGH

### TC047: Layoff Supervisor - Opening Under Same VP
- **Objective:** Supervisor layoff logic
- **Preconditions:** VP has opening for supervisor
- **Steps:** LAYOFF VP SupervisorName
- **Expected Result:** Supervisor moved to opening under same VP
- **Priority:** MEDIUM

### TC048: Layoff Supervisor - Opening Under Different VP
- **Objective:** Cross-VP supervisor movement
- **Preconditions:** No opening under same VP, opening under other VP
- **Steps:** LAYOFF
- **Expected Result:** Supervisor moves to other VP
- **Priority:** MEDIUM

### TC049: Layoff VP - Opening Available
- **Objective:** VP layoff with opening
- **Preconditions:** President has VP vacancy
- **Steps:** LAYOFF President VPName
- **Expected Result:** VP moved to vacancy
- **Priority:** MEDIUM

### TC050: Layoff VP - No Opening
- **Objective:** VP removal when full
- **Preconditions:** President has 2 VPs (full)
- **Steps:** LAYOFF President VP1
- **Expected Result:** VP1 removed permanently
- **Priority:** MEDIUM

### TC051: Layoff Outside Hierarchy
- **Objective:** Verify authorization
- **Preconditions:** VP1, VP2 as peers
- **Steps:** VP1 attempts layoff of VP2's employee
- **Expected Result:** Error: not in hierarchy
- **Priority:** HIGH

### TC052: Layoff President
- **Objective:** President protection
- **Steps:** LAYOFF President President
- **Expected Result:** Error: cannot lay off president
- **Priority:** MEDIUM

---

## CATEGORY F: TRANSFER OPERATIONS (TC053-TC062)

### TC053: VP Transfers Supervisor Within Own Organization
- **Objective:** Valid lateral transfer
- **Preconditions:** 
  - VP has 2 supervisors
  - VP has vacancy for 3rd supervisor
- **Steps:** TRANSFER VP Supervisor1 VP (to vacancy)
- **Expected Result:** Success message (though logically same position)
- **Priority:** MEDIUM

### TC054: President Transfers VP Between VPs
- **Objective:** President authority to transfer anyone
- **Preconditions:** VP1 has supervisor, VP2 has vacancy
- **Steps:** TRANSFER President Supervisor1 VP2
- **Expected Result:** Supervisor moves from VP1 to VP2
- **Priority:** HIGH

### TC055: President Transfers Worker Across Organization
- **Objective:** Cross-organization worker transfer
- **Preconditions:** Worker under Supervisor1, Supervisor2 has vacancy
- **Steps:** TRANSFER President Worker1 Supervisor2
- **Expected Result:** Worker moves to Supervisor2
- **Priority:** HIGH

### TC056: VP Transfers Within Own Hierarchy
- **Objective:** VP transferring workers between own supervisors
- **Preconditions:** VP has 2 supervisors, Supervisor1 has worker, Supervisor2 has vacancy
- **Steps:** TRANSFER VP Worker1 Supervisor2
- **Expected Result:** Worker transfers successfully
- **Priority:** HIGH

### TC057: Supervisor Attempts Transfer
- **Objective:** Verify only VP/President can transfer
- **Preconditions:** Supervisor exists
- **Steps:** TRANSFER Supervisor Worker NewSupervisor
- **Expected Result:** Error: no permission to transfer
- **Priority:** HIGH

### TC058: Worker Attempts Transfer
- **Objective:** Verify workers cannot transfer
- **Preconditions:** Worker exists
- **Steps:** TRANSFER Worker SomeEmployee Somewhere
- **Expected Result:** Error: no permission
- **Priority:** MEDIUM

### TC059: Transfer to Non-Vacant Position
- **Objective:** Verify vacancy requirement
- **Preconditions:** Destination position full
- **Steps:** TRANSFER President Worker FullSupervisor
- **Expected Result:** Error: maximum direct reports reached
- **Priority:** HIGH

### TC060: Transfer with Role Mismatch
- **Objective:** Verify same-level requirement
- **Preconditions:** Attempt to transfer worker to VP position
- **Steps:** TRANSFER President Worker President (wrong level)
- **Expected Result:** Error: role mismatch
- **Priority:** HIGH

### TC061: Transfer Outside Initiator's Authority
- **Objective:** Verify initiator manages both spots
- **Preconditions:** VP1 tries to transfer employee from VP2's hierarchy
- **Steps:** TRANSFER VP1 VP2Employee Somewhere
- **Expected Result:** Error: does not manage employee
- **Priority:** HIGH

### TC062: Transfer with Non-Existent Participants
- **Objective:** Validate all participants exist
- **Steps:** TRANSFER Ghost1 Ghost2 Ghost3
- **Expected Result:** Error: does not exist
- **Priority:** MEDIUM

---

## CATEGORY G: PROMOTE OPERATIONS (TC063-TC072)

### TC063: Promote Worker to Supervisor
- **Objective:** Valid one-level promotion
- **Preconditions:** VP has supervisor vacancy, worker exists elsewhere
- **Steps:** PROMOTE VP WorkerName
- **Expected Result:** Worker promoted to supervisor under VP
- **Priority:** HIGH

### TC064: Promote Supervisor to VP
- **Objective:** Supervisor to VP promotion
- **Preconditions:** President has VP vacancy, supervisor exists
- **Steps:** PROMOTE President SupervisorName
- **Expected Result:** Supervisor promoted to VP
- **Priority:** HIGH

### TC065: Attempt to Promote Worker to VP (2 Levels)
- **Objective:** Verify one-level rule
- **Preconditions:** Worker exists, president has vacancy
- **Steps:** PROMOTE President WorkerName
- **Expected Result:** Error: promotions can only be one level
- **Priority:** HIGH

### TC066: Attempt to Promote VP to President
- **Objective:** Verify cannot promote to president
- **Preconditions:** VP exists
- **Steps:** PROMOTE ??? VP (no valid receiving manager)
- **Expected Result:** Error: cannot be promoted further
- **Priority:** HIGH

### TC067: Promote to Same Organization (Peer Prevention)
- **Objective:** Verify no supervision of former peers
- **Preconditions:** Worker1, Worker2 under Supervisor1, Supervisor1 has vacancy
- **Steps:** PROMOTE Supervisor1 Worker1 (would supervise Worker2)
- **Expected Result:** Error or promotion blocked
- **Priority:** HIGH

### TC068: Promote Without Vacancy
- **Objective:** Verify vacancy requirement
- **Preconditions:** Receiving manager at capacity
- **Steps:** PROMOTE FullManager Employee
- **Expected Result:** Error: maximum direct reports reached
- **Priority:** HIGH

### TC069: Worker/Supervisor as Receiving Manager
- **Objective:** Verify only VP/President can be receiving manager
- **Preconditions:** Supervisor exists
- **Steps:** PROMOTE Supervisor Employee
- **Expected Result:** Error: cannot promote employees
- **Priority:** MEDIUM

### TC070: Promote Employee Who Has Reports
- **Objective:** Vacancy created in old position
- **Preconditions:** Supervisor with workers gets promoted
- **Steps:** PROMOTE President SupervisorWithWorkers
- **Expected Result:** Promoted, vacancy created, workers remain under vacancy
- **Priority:** HIGH

### TC071: Promote with Non-Existent Employee
- **Objective:** Validate employee exists
- **Steps:** PROMOTE VP GhostEmployee
- **Expected Result:** Error: does not exist
- **Priority:** MEDIUM

### TC072: Promote with Non-Existent Manager
- **Objective:** Validate receiving manager exists
- **Steps:** PROMOTE GhostManager Employee
- **Expected Result:** Error: does not exist
- **Priority:** MEDIUM

---

## CATEGORY H: DISPLAY OPERATIONS (TC073-TC080)

### TC073: Display Full Organization
- **Objective:** Verify complete hierarchy display
- **Preconditions:** Full organization with all levels
- **Steps:** DISPLAY
- **Expected Result:** Proper indentation, all roles and names shown
- **Priority:** HIGH

### TC074: Display with Vacancies
- **Objective:** Verify vacancy display format
- **Preconditions:** Organization with supervisor vacancies
- **Steps:** DISPLAY
- **Expected Result:** "VACANCY: [Role]" shown with proper indentation
- **Priority:** HIGH

### TC075: Display Does Not Show Worker Vacancies
- **Objective:** Verify worker vacancies hidden per SRS 11b
- **Preconditions:** Supervisor with only 3 of 5 workers
- **Steps:** DISPLAY
- **Expected Result:** Shows 3 workers, no vacancy lines
- **Priority:** MEDIUM

### TC076: Display Hides Completely Vacant Branches
- **Objective:** Per SRS 11b, don't show vacant subordinates
- **Preconditions:** VP vacancy with no supervisors beneath
- **Steps:** DISPLAY
- **Expected Result:** VP vacancy shown, but no empty structure beneath
- **Priority:** MEDIUM

### TC077: Display with Tabs vs Spaces Indentation
- **Objective:** Verify indentation format
- **Preconditions:** Multi-level organization
- **Steps:** DISPLAY and inspect output
- **Expected Result:** Tabs used for indentation (per code)
- **Priority:** LOW

### TC078: Display Proper Role Labels
- **Objective:** Verify role names correct
- **Preconditions:** All role types present
- **Steps:** DISPLAY
- **Expected Result:** "President:", "Vice President:", "Supervisor:", "Worker:"
- **Priority:** MEDIUM

### TC079: Display After Complex Operations
- **Objective:** State consistency verification
- **Preconditions:** Perform multiple hire/fire/promote
- **Steps:** 
  1. Execute 10+ operations
  2. DISPLAY
- **Expected Result:** Accurate current state shown
- **Priority:** MEDIUM

### TC080: Display Empty Organization (No President)
- **Objective:** Handle edge case
- **Preconditions:** No initialization
- **Steps:** DISPLAY before initializing president
- **Expected Result:** "Organization is empty" or similar
- **Priority:** LOW

---

## SUMMARY

**Total Test Cases: 80**

### Priority Breakdown:
- **HIGH Priority:** 42 test cases (critical functionality, SRS requirements)
- **MEDIUM Priority:** 28 test cases (important edge cases, error handling)
- **LOW Priority:** 10 test cases (nice-to-have validations)

### Coverage by Requirement:
- Req 1 (Hierarchy): TC001-TC010, TC073-TC080
- Req 2 (Unique Names): TC002, TC003, TC020, TC023, TC024
- Req 3 (Hiring): TC011-TC025
- Req 4 (Firing): TC026-TC035
- Req 5 (Quitting): TC036-TC042
- Req 6 (Layoff): TC043-TC052
- Req 7 (Transfer): TC053-TC062
- Req 8 (Promote): TC063-TC072
- Req 9 (File I/O): NOT IMPLEMENTED - Out of Scope
- Req 10 (Commands): All TCs
- Req 11 (Display): TC073-TC080



