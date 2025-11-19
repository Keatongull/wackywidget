# Wacky Widget Organization Management System - Test Suite

## Overview

This repository contains a comprehensive black box test suite for the Wacky Widget Organization Management System. The test suite includes 148 unique tests covering all operations, edge cases, and bug detection scenarios.

## Running the Tests

### Basic Test Execution

To run all tests with full output:

**Windows (PowerShell):**
```powershell
python run_blackbox_tests.py
```

**Mac/Linux (bash/zsh):**
```bash
python run_blackbox_tests.py
```

### Display Options

> **Note for Mac/Linux users:** The commands below show both Windows PowerShell and Mac/Linux bash/zsh equivalents.

#### 1. **View Only Summary Statistics**
**Windows:**
```powershell
python run_blackbox_tests.py 2>&1 | Select-String -Pattern "Total Tests|Passed:|Failed:|Pass Rate"
```
**Mac/Linux:**
```bash
python run_blackbox_tests.py 2>&1 | grep -E "Total Tests|Passed:|Failed:|Pass Rate"
```

#### 2. **View Last 50 Lines (Summary + Recent Tests)**
**Windows:**
```powershell
python run_blackbox_tests.py 2>&1 | Select-Object -Last 50
```
**Mac/Linux:**
```bash
python run_blackbox_tests.py 2>&1 | tail -50
```

#### 3. **View Last 100 Lines (More Context)**
**Windows:**
```powershell
python run_blackbox_tests.py 2>&1 | Select-Object -Last 100
```
**Mac/Linux:**
```bash
python run_blackbox_tests.py 2>&1 | tail -100
```

#### 4. **View Only Failed Tests**
**Windows:**
```powershell
python run_blackbox_tests.py 2>&1 | Select-String -Pattern "\[FAIL\]"
```
**Mac/Linux:**
```bash
python run_blackbox_tests.py 2>&1 | grep "\[FAIL\]"
```

#### 5. **View Only Passed Tests**
**Windows:**
```powershell
python run_blackbox_tests.py 2>&1 | Select-String -Pattern "\[PASS\]"
```
**Mac/Linux:**
```bash
python run_blackbox_tests.py 2>&1 | grep "\[PASS\]"
```

#### 6. **Count Pass/Fail**
**Windows:**
```powershell
python run_blackbox_tests.py 2>&1 | Select-String -Pattern "PASSED|FAILED" | Measure-Object -Line
```
**Mac/Linux:**
```bash
python run_blackbox_tests.py 2>&1 | grep -E "PASSED|FAILED" | wc -l
```

#### 7. **View Specific Test Category**
**Windows:**
```powershell
# Example: View only HIRE tests
python run_blackbox_tests.py 2>&1 | Select-String -Pattern "BBT00[4-9]|BBT01[0-3]"
```
**Mac/Linux:**
```bash
# Example: View only HIRE tests
python run_blackbox_tests.py 2>&1 | grep -E "BBT00[4-9]|BBT01[0-3]"
```

#### 8. **Save Full Output to File**
**Windows:**
```powershell
python run_blackbox_tests.py > test_results.txt 2>&1
```
**Mac/Linux:**
```bash
python run_blackbox_tests.py > test_results.txt 2>&1
```

#### 9. **View Failed Tests List Only**
**Windows:**
```powershell
python run_blackbox_tests.py 2>&1 | Select-Object -Last 40 | Select-Object -First 35
```
**Mac/Linux:**
```bash
python run_blackbox_tests.py 2>&1 | tail -40 | head -35
```

#### 10. **Real-time Monitoring (Watch Mode)**
**Windows:**
```powershell
python run_blackbox_tests.py 2>&1 | Tee-Object -FilePath test_results.txt
```
**Mac/Linux:**
```bash
python run_blackbox_tests.py 2>&1 | tee test_results.txt
```

## Test Suite Organization

The test suite contains **148 tests** organized into the following categories:

### Initialization Tests (BBT001-BBT003C)
- President initialization
- Name validation
- Empty/invalid names

### HIRE Operation Tests (BBT004-BBT013B)
- Capacity limits at all levels
- Duplicate name detection
- Invalid manager checks
- Worker hiring restrictions

### FIRE Operation Tests (BBT014-BBT018)
- Employee removal
- Vacancy creation
- Hierarchy enforcement
- President protection

### QUIT Operation Tests (BBT019-BBT021E)
- Voluntary resignation
- Vacancy handling
- President restrictions

### LAYOFF Operation Tests (BBT022-BBT024A)
- Opening search priority
- Employee relocation
- No-opening scenarios

### TRANSFER Operation Tests (BBT025-BBT028)
- Cross-hierarchy transfers
- Permission validation
- Capacity enforcement

### PROMOTE Operation Tests (BBT029-BBT044)
- Level-by-level promotion
- Vacancy requirements
- Capacity limits

### Name Validation Tests (BBT045-BBT052, BBT081-BBT089)
- Names with spaces
- Numeric names
- Special characters
- Edge cases

### Hierarchy Display Tests (BBT053-BBT080)
- Vacancy display
- Subordinate preservation
- Deep hierarchy handling

### Complex Workflow Tests (BBT059-BBT079)
- Multi-operation sequences
- State consistency
- Edge case combinations

### Advanced Bug Detection Tests (BBT090-BBT150)
- Subordinate handling after removal
- Name reuse scenarios
- Circular reporting prevention
- Capacity enforcement edge cases
- Vacancy operations
- Deep hierarchy scenarios

## Test Results Interpretation

### Pass Rate Indicators
- **90-100%**: Excellent - Production ready
- **80-89%**: Good - Minor bugs exist
- **70-79%**: Fair - Moderate bugs identified
- **Below 70%**: Poor - Major issues present

### Current Status
As of the latest run:
- **Total Tests:** 148
- **Passed:** 117
- **Failed:** 31
- **Pass Rate:** 79.1%

### Known Bug Categories (31 Failed Tests)
1. **Name Validation Issues** - System accepts invalid names (spaces, numbers, special characters)
2. **Hierarchy Display Bugs** - Subordinates disappear when managers are removed
3. **Case Sensitivity Issues** - Same names with different cases treated as different people
4. **Invalid Hierarchy Creation** - Promotion can create VP under VP structures

## Requirements

- Python 3.x
- **Windows:** PowerShell (for display formatting commands)
- **Mac/Linux:** bash or zsh shell (for display formatting commands)
- The main.py program must be in the same directory

## Test Output Format

Each test displays:
```
======================================================================
Running BBT###: Test Description
======================================================================
Input commands: [list of commands]

Program output:
[actual program output]

[PASS/FAIL] Expected: 'text' - FOUND/NOT FOUND

[PASS/FAIL] BBT### PASSED/FAILED
```

## Exit Codes

- `0` - All tests passed
- `1` - One or more tests failed

## Troubleshooting

### Tests Timeout
If tests hang, the default timeout is 5 seconds per test. Check for:
- Infinite loops in the main program
- Input prompts that aren't being satisfied

### Import Errors
Ensure `main.py`, `employee.py`, and `organization_manager.py` are in the same directory.

### PowerShell Command Issues
If PowerShell commands don't work, try running from a PowerShell terminal (not CMD).

### Mac/Linux Command Issues
If you're on Mac/Linux and the bash commands don't work, ensure you're using bash or zsh (not fish or another shell).

## Contributing

When adding new tests:
1. Follow the existing naming convention (BBT###)
2. Provide clear test descriptions
3. Include expected output strings
4. Group related tests together
5. Update this README with new test categories
