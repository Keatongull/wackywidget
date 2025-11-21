# Wacky Widget Organization - Black Box Test Results

**Testing Phase:** Independent Verification  
**Version / Build:** v1.0  
**Testers:** Keaton, Tyler, Kayd, Eric  
**Environment:** Python 3.x CLI  

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

- Total Tests: 148
- Passed: 117
- Failed: 31
- Pass Rate: 79.1%

**Module Coverage**
- Initialization: 6 tests
- Hire: 12 tests
- Fire: 5 tests
- Quit: 7 tests
- Layoff: 4 tests
- Transfer: 4 tests
- Promotion: 16 tests
- Name Validation: 12 tests
- Heirarchy Display: 6 tests
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
| BBT027 | Supervisor cannot transfer | Pass | High | — | — |
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
A total of 30 defects (BUG-001 → BUG-030) were identified across the Wacky Widget Organization System.
These span Display, Name Validation, Hire/Fire/Layoff Operations, Initialization, and Promotion Logic.

**Severity distribution:**
- Critical: 13
- Major: 8
- Minor: 9

The most serious issues involve loss of subordinate data, display corruption, invalid promotions, and unsafe name validation.

**Critical issues** affect core functionality such as display corruption, subordinate loss, invalid hierarchy formation, and unsafe input handling.  
**Major issues** include invalid name acceptance, improper handling of hires and layoffs, and display failures under complex structures.  
**Minor issues** relate to whitespace handling, name formatting, and multi-vacancy display edge cases.

**Critical Bugs**
- BUG-001: Subordinates disappear after FIRE
- BUG-007: VP can promote Supervisor into invalid VP → VP hierarchy
- BUG-008: Unlimited promotions break hierarchy rules
- BUG-011: Cascading fires delete entire subtree
- BUG-012: Layoff operation deletes subordinates
- BUG-013: Display stops recursing at vacancy
- BUG-022: SQL injection attempt accepted
- BUG-026: Nested vacancy display completely broken
- BUG-027: Layoff VP → all subordinates gone
- BUG-028: Deep hierarchy collapses after FIRE
- BUG-029: Supervisor FIRE loses workers
- BUG-030: VP quit loses subordinate visibility

## 6. Observations
- **Display Issues:** Multiple critical bugs (BUG-001, BUG-030, BUG-026) show that the display loop does not recurse correctly through vacancies and subordinates. Recommend immediate fix before release.  
- **Input Validation:** System currently allows numeric-only names, special characters, and whitespace-only names (BUG-002, BUG-003, BUG-017). Input sanitization should be strengthened.  
- **Hierarchy Rules:** Promotion logic allows creation of invalid VP hierarchy (BUG-007, BUG-008). Level validation needed in your promote employee functionality.
- **Specification Issues:** Many implementation bugs trace back to ambiguous or contradictory requirements (see Section 4). A significant portion of defects could have been prevented with clearer SRS documentation.
- **Overall:** While basic hire/fire functionality works, critical bugs in display, input validation, and hierarchy may confuse users and violate SRS requirements.  

## 7. Final Assessment of Quality
Overall, the Wacky Widget Organization system demonstrates partial compliance with the expected functional requirements. While core features such as basic hiring, firing, quitting, and simple promotions work under normal conditions, the system exhibits significant quality issues when exposed to edge cases, invalid input, vacancy propagation, and deeper hierarchical operations.

**Strengths**  
- Basic CRUD operations (hire/fire/quit) work reliably in standard scenarios.
- The system accepts a wide range of commands consistently.
- Most simple hierarchical transitions behave as expected.

**Major Quality Concerns**  
- Hierarchy Corruption: Several operations (fire, quit, layoff) cause subtrees to disappear or collapse.
- Display Instability: The display function fails to traverse all levels, breaks on vacancies, and loses subordinates.
- Weak Input Validation: Numeric names, special characters, SQL-injection-like input, whitespace-only names, and escape sequences are accepted.
- Promotion Rule Violations: Promotions can create invalid hierarchies or skip levels.
- Inconsistent Vacancy Handling: Vacancies can break traversal, corrupt display, or incorrectly delete subordinates.

**Release Readiness**  
In its current state, the system is not ready for production or classroom demo use, particularly due to issues that compromise:
- correctness of displayed information,
- structural integrity of the hierarchy, and
- safety and validity of user input.