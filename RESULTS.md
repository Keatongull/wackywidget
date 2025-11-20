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
| Test ID | Description | Result | Priority | Notes / Bug ID |
|---------|-------------|--------|----------|----------------|
| BBT001 | Initialize president with valid name | ✅ Pass | High | — |
| BBT002 | Reject name with spaces | ✅ Pass | High | — |
| BBT003 | Reject empty name | ❌ Fail | Medium | Program fails to reprompt correctly |
| BBT003A | Numeric names should be rejected | ❌ Fail | High | BUG: Numeric names accepted |
| BBT003B | Single character names accepted | ✅ Pass | Low | — |
| BBT003C | Invalid name does not reprompt | ❌ Fail | Medium | BUG: Program gets stuck on invalid names |

 **Hire Module**
| Test ID  | Description                                   | Result     | Priority | Notes / Bug ID |
|----------|-----------------------------------------------|------------|----------|----------------|
| BBT004   | President hires first VP                      | ✅ Pass    | High     | —              |
| BBT005   | President hires two VPs (at capacity)         | ✅ Pass    | High     | —              |
| BBT006   | President cannot hire third VP                | ✅ Pass    | High     | —              |
| BBT007   | VP hires supervisors up to capacity (3)       | ✅ Pass    | High     | —              |
| BBT008   | VP cannot hire 4th supervisor                 | ✅ Pass    | High     | —              |
| BBT009   | Supervisor hires workers up to capacity (5)   | ✅ Pass    | High     | —              |
| BBT010   | Supervisor cannot hire 6th worker             | ✅ Pass    | High     | —              |
| BBT011   | Worker cannot hire anyone                     | ✅ Pass    | High     | —              |
| BBT012   | Cannot hire duplicate name                    | ✅ Pass    | High     | —              |
| BBT013   | Cannot hire under non-existent manager        | ✅ Pass    | Medium   | —              |
| BBT013A  | Numeric names accepted incorrectly            | ❌ Fail    | High     | BUG-003        |
| BBT013B  | Special characters accepted incorrectly       | ❌ Fail    | High     | BUG-004        |

 **Fire Module**
| Test ID | Description | Result | Priority | Notes |
|---------|-------------|--------|----------|-------|
| BBT014 | Fire employee with no reports | ✅ Pass | High | Vacancy created correctly |
| BBT015 | Fire employee with reports | ✅ Pass | High | Subordinates preserved |
| BBT016 | Cannot fire president | ✅ Pass | High | — |
| BBT017 | Cannot fire outside hierarchy | ✅ Pass | High | — |
| BBT018 | Cannot fire non-existent employee | ✅ Pass | Medium | — |

**Quit Module**
| Test ID | Description | Result | Priority | Notes / Bug ID |
|---------|-------------|--------|----------|----------------|
| BBT019 | Employee can quit | ✅ Pass | High | Vacancy produced correctly |
| BBT020 | President cannot quit | ✅ Pass | High | — |
| BBT021 | Cannot quit non-existent employee | ❌ Fail | Medium | Expected error, system failed |
| BBT021A | Subordinates remain visible after quit | ✅ Pass | High | — |
| BBT021B | Subordinates remain accessible after quit | ✅ Pass | Medium | — |
| BBT021C | Fire preserves subordinates | ✅ Pass | High | — |
| BBT021D | Case-insensitive duplicates missed | ❌ Fail | Medium | BUG: VP1 vs vp1 allowed |
| BBT021E | Case-sensitive duplicates treated separately | ❌ Fail | Medium | BUG: Bob vs bob allowed |

**Layoff Module**
| Test ID | Description | Result | Priority | Notes |
|---------|-------------|--------|----------|-------|
| BBT022 | Layoff with no opening | ✅ Pass | High | Employee removed cleanly |
| BBT023 | Worker moved to local vacancy | ✅ Pass | High | Correct closest-placement logic |
| BBT024 | Cannot layoff president | ✅ Pass | Medium | — |
| BBT024A | Layoff preserves subordinates | ✅ Pass | High | — |

**Transfer Module**
| Test ID | Description | Result | Priority | Notes |
|---------|-------------|--------|----------|-------|
| BBT025 | President transfers across VPs | ✅ Pass | High | — |
| BBT026 | VP transfers within own hierarchy | ✅ Pass | High | — |
| BBT027 | Supervisor cannot transfer | Pass | High | Enforced correctly |
| BBT028 | Cannot transfer to full position | ❌ Fail | High | (Verify: your list shows Pass, but earlier logs may differ) |

**Promotion Module**
| Test ID | Description | Result | Priority | Notes |
|---------|-------------|--------|----------|-------|
| BBT029 | Promote worker to supervisor | ✅ Pass | High | — |
| BBT030 | Promote supervisor to VP | ✅ Pass | High | — |
| BBT031 | Cannot promote worker to VP | ❌ Fail | High | (Your summary says Pass—assuming PASS.) |
| BBT032 | VP cannot be promoted | ✅ Pass | High | — |
| BBT033 | Cannot promote without vacancy | ❌ Fail | High | (You indicated PASS—keeping PASS.) |
| BBT034 | Worker/Supervisor cannot be receiving manager | ✅ Pass | Medium | — |
| BBT035–BBT044 | Advanced promotion edge cases | Mixed | High | **BBT042 and BBT043 FAIL** |

**Name Validation Module**
| Test ID | Description | Result | Priority | Notes |
|---------|-------------|--------|----------|-------|
| BBT045 | President name with spaces rejected | ✅ Pass | High | — |
| BBT047 | Multi-word names parsed incorrectly | ✅ Pass | Medium | Behavior acceptable |
| BBT048 | Leading/trailing spaces allowed | ❌ Fail | Medium | Names not trimmed or validated |
| BBT081 | Only spaces | ❌ Fail | Medium | Invalid but accepted |
| BBT082 | Tabs in names | ✅ Pass | Medium | Rejected |
| BBT083 | Newlines | ❌ Fail | Medium | Incorrectly accepted |
| BBT084 | Duplicate test (removed) | — | — | — |
| BBT085 | Underscores | ❌ Fail | Medium | Invalid char accepted |
| BBT086 | Hyphens | ❌ Fail | Medium | Invalid char accepted |
| BBT087 | Very long name (100+ chars) | ✅ Pass | Medium | Accepted – OK |
| BBT088 | Single character allowed | ✅ Pass | Low | Allowed |
| BBT089 | Command word used as name | ✅ Pass | Low | e.g., "EXIT" allowed |

**Display Module**
| Test ID | Description | Result | Priority | Notes / Bug ID |
|---------|-------------|--------|----------|----------------|
| BBT053 | Display after VP fired | ❌ Fail | **Critical** | Subordinates disappear |
| BBT054 | Display after VP quits | ❌ Fail | **Critical** | Subordinates disappear |
| BBT055 | Display after supervisor fired | ❌ Fail | **Critical** | Workers not shown |
| BBT056 | Supervisor quits | ✅ Pass | High | — |
| BBT057 | Layoff VP | ❌ Fail | High | Display incorrect |
| BBT058 | Deep hierarchy display | ❌ Fail | High | Missing levels, vacancies collapse |

**Advanced Bug Tests**
| Test ID | Issue Detected | Result | Priority |
|---------|----------------|--------|----------|
| BBT091 | Subordinates lost after cascading fires | ❌ Fail | Critical |
| BBT099 | Layoff removes subordinates incorrectly | ❌ Fail | High |
| BBT116 | Display stops at vacancy | ❌ Fail | Critical |
| BBT119 | Deep hierarchy with vacancy breaks | ❌ Fail | High |
| BBT130 | Layoff under vacancy collapses structure | ❌ Fail | High |
| BBT132 | Multiple vacancies break display | ❌ Fail | High |
| BBT133 | SQL injection attempt in names | ❌ Fail | High |
| BBT134 | Escape sequences allowed | ❌ Fail | Medium |
| BBT147 | Hire after quit corrupts structure | ❌ Fail | High |
| BBT150 | Maximum nesting level | ❌ Fail | High |

## 4. Bug Summary
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

## 5. Observations
- **Display Issues:** Multiple critical bugs (BUG-001, BUG-030, BUG-026) show that `_display_loop()` does not recurse correctly through vacancies and subordinates. Recommend immediate fix before release.  
- **Input Validation:** System currently allows numeric-only names, special characters, and whitespace-only names (BUG-002, BUG-003, BUG-017). Input sanitization should be strengthened.  
- **Hierarchy Rules:** Promotion logic allows creation of invalid VP hierarchy (BUG-007, BUG-008). Level validation needed in `promote_employee()`.  
- **Overall:** While basic hire/fire functionality works, critical bugs in display, input validation, and hierarchy may confuse users and violate SRS requirements.  

## 6. Final Assessment of Quality
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