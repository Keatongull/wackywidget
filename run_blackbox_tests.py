"""
Black Box Test Automation for Wacky Widget Organization
Independent testing - does NOT import their code, tests only via CLI interface
Team 2 - Independent Verification
"""

import subprocess
import sys
from typing import List, Tuple


class BlackBoxTester:
    """Runs the main.py program and interacts via stdin/stdout"""
    
    def __init__(self):
        self.test_results = []
        self.passed = 0
        self.failed = 0
        
    def run_test(self, test_id: str, description: str, 
                 inputs: List[str], expected_outputs: List[str],
                 should_contain_all: bool = False) -> bool:
        """
        Run a single black box test
        
        Args:
            test_id: Test identifier
            description: What this test validates
            inputs: List of commands to send to the program
            expected_outputs: List of strings that should appear in output
            should_contain_all: If True, ALL expected outputs must be present
        """
        print(f"\n{'='*70}")
        print(f"Running {test_id}: {description}")
        print(f"{'='*70}")
        
        # Prepare input
        all_input = "\n".join(inputs) + "\n"
        
        try:
            # Run the program as a black box
            result = subprocess.run(
                [sys.executable, "main.py"],
                input=all_input,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            output = result.stdout + result.stderr
            
            print(f"Input commands: {inputs}")
            print(f"\nProgram output:\n{output}")
            
            # Check if expected outputs are present
            matches = []
            for expected in expected_outputs:
                found = expected.lower() in output.lower()
                matches.append(found)
                status = "[PASS]" if found else "[FAIL]"
                print(f"{status} Expected: '{expected}' - {'FOUND' if found else 'NOT FOUND'}")
            
            # Determine pass/fail
            if should_contain_all:
                passed = all(matches)
            else:
                passed = any(matches)
            
            # Record result
            self.test_results.append({
                'id': test_id,
                'description': description,
                'passed': passed,
                'output': output
            })
            
            if passed:
                self.passed += 1
                print(f"\n[PASS] {test_id} PASSED")
            else:
                self.failed += 1
                print(f"\n[FAIL] {test_id} FAILED")
            
            return passed
            
        except subprocess.TimeoutExpired:
            print(f"\n[FAIL] {test_id} FAILED - Program timed out")
            self.failed += 1
            self.test_results.append({
                'id': test_id,
                'description': description,
                'passed': False,
                'output': 'TIMEOUT'
            })
            return False
        except Exception as e:
            print(f"\n[FAIL] {test_id} FAILED - Exception: {e}")
            self.failed += 1
            self.test_results.append({
                'id': test_id,
                'description': description,
                'passed': False,
                'output': f'EXCEPTION: {e}'
            })
            return False
    
    def print_summary(self):
        """Print test execution summary"""
        print("\n" + "="*70)
        print("TEST EXECUTION SUMMARY")
        print("="*70)
        print(f"Total Tests: {self.passed + self.failed}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        if self.passed + self.failed > 0:
            pass_rate = (self.passed / (self.passed + self.failed)) * 100
            print(f"Pass Rate: {pass_rate:.1f}%")
        print("="*70)
        
        if self.failed > 0:
            print("\nFAILED TESTS:")
            for result in self.test_results:
                if not result['passed']:
                    print(f"  - {result['id']}: {result['description']}")


def main():
    """Run all black box tests"""
    tester = BlackBoxTester()
    
    # ========== INITIALIZATION TESTS ==========
    
    tester.run_test(
        "BBT001",
        "Initialize president with valid name",
        ["Alice", "DISPLAY", "EXIT"],
        ["President: Alice"]
    )
    
    tester.run_test(
        "BBT002",
        "Reject name with spaces",
        ["Bob Smith", "EXIT"],
        ["Error", "Invalid"]
    )
    
    tester.run_test(
        "BBT003",
        "Reject empty name",
        ["", "Alice", "EXIT"],
        ["President: Alice"]
    )
    
    tester.run_test(
        "BBT003A",
        "BUG: Numeric names should be rejected",
        ["123", "DISPLAY", "EXIT"],
        ["Error", "Invalid"]  # Should reject numeric names
    )
    
    tester.run_test(
        "BBT003B",
        "BUG: Single character names accepted",
        ["X", "DISPLAY", "EXIT"],
        ["President: X"]  # May or may not be a bug depending on requirements
    )
    
    tester.run_test(
        "BBT003C",
        "BUG: Invalid president name doesn't reprompt - program stuck",
        ["", "", "ValidName", "EXIT"],
        ["President: ValidName"]  # Should eventually accept valid name after rejecting invalid
    )
    
    # ========== HIRE TESTS ==========
    
    tester.run_test(
        "BBT004",
        "President hires first VP",
        ["President1", "HIRE President1 VP1", "DISPLAY", "EXIT"],
        ["Vice President: VP1", "Successfully"]
    )
    
    tester.run_test(
        "BBT005",
        "President hires two VPs (at capacity)",
        ["President1", "HIRE President1 VP1", "HIRE President1 VP2", 
         "DISPLAY", "EXIT"],
        ["Vice President: VP1", "Vice President: VP2"]
    )
    
    tester.run_test(
        "BBT006",
        "President cannot hire third VP (over capacity)",
        ["President1", "HIRE President1 VP1", "HIRE President1 VP2",
         "HIRE President1 VP3", "EXIT"],
        ["maximum direct reports", "Error"]
    )
    
    tester.run_test(
        "BBT007",
        "VP hires supervisors up to capacity (3)",
        ["President1", "HIRE President1 VP1", 
         "HIRE VP1 S1", "HIRE VP1 S2", "HIRE VP1 S3",
         "DISPLAY", "EXIT"],
        ["Supervisor: S1", "Supervisor: S2", "Supervisor: S3"]
    )
    
    tester.run_test(
        "BBT008",
        "VP cannot hire 4th supervisor",
        ["President1", "HIRE President1 VP1",
         "HIRE VP1 S1", "HIRE VP1 S2", "HIRE VP1 S3", "HIRE VP1 S4",
         "EXIT"],
        ["maximum direct reports", "Error"]
    )
    
    tester.run_test(
        "BBT009",
        "Supervisor hires workers up to capacity (5)",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1",
         "HIRE S1 W1", "HIRE S1 W2", "HIRE S1 W3", "HIRE S1 W4", "HIRE S1 W5",
         "DISPLAY", "EXIT"],
        ["Worker: W5", "Successfully"]
    )
    
    tester.run_test(
        "BBT010",
        "Supervisor cannot hire 6th worker",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1",
         "HIRE S1 W1", "HIRE S1 W2", "HIRE S1 W3", "HIRE S1 W4", "HIRE S1 W5",
         "HIRE S1 W6", "EXIT"],
        ["maximum direct reports", "Error"]
    )
    
    tester.run_test(
        "BBT011",
        "Worker cannot hire anyone",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1", "HIRE S1 W1",
         "HIRE W1 Intern", "EXIT"],
        ["cannot hire", "Error"]
    )
    
    tester.run_test(
        "BBT012",
        "Cannot hire duplicate name",
        ["President1", "HIRE President1 VP1", "HIRE President1 VP1", "EXIT"],
        ["already exists", "Error"]
    )
    
    tester.run_test(
        "BBT013",
        "Cannot hire under non-existent manager",
        ["President1", "HIRE GhostManager NewPerson", "EXIT"],
        ["does not exist", "Error"]
    )
    
    tester.run_test(
        "BBT013A",
        "BUG: Can hire employees with numeric names",
        ["President1", "HIRE President1 999", "EXIT"],
        ["Error", "Invalid"]  # Should reject numeric names
    )
    
    tester.run_test(
        "BBT013B",
        "BUG: Can hire employees with special characters",
        ["President1", "HIRE President1 Test@123", "EXIT"],
        ["Error", "Invalid"]  # Should reject special characters in names
    )
    
    # ========== FIRE TESTS ==========
    
    tester.run_test(
        "BBT014",
        "Fire employee with no reports",
        ["President1", "HIRE President1 VP1", "FIRE President1 VP1",
         "DISPLAY", "EXIT"],
        ["removed", "VACANCY: Vice President"]
    )
    
    tester.run_test(
        "BBT015",
        "Fire employee with reports creates vacancy",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1",
         "FIRE President1 VP1", "DISPLAY", "EXIT"],
        ["VACANCY: Vice President", "Supervisor: S1"]
    )
    
    tester.run_test(
        "BBT016",
        "Cannot fire president",
        ["President1", "FIRE President1 President1", "EXIT"],
        ["Cannot fire the President", "Error"]
    )
    
    tester.run_test(
        "BBT017",
        "Cannot fire outside hierarchy",
        ["President1", "HIRE President1 VP1", "HIRE President1 VP2",
         "HIRE VP1 S1", "FIRE VP2 S1", "EXIT"],
        ["not in the hierarchy", "Error"]
    )
    
    tester.run_test(
        "BBT018",
        "Cannot fire non-existent employee",
        ["President1", "FIRE President1 Ghost", "EXIT"],
        ["does not exist", "Error"]
    )
    
    # ========== QUIT TESTS ==========
    
    tester.run_test(
        "BBT019",
        "Employee can quit",
        ["President1", "HIRE President1 VP1", "QUIT VP1",
         "DISPLAY", "EXIT"],
        ["removed", "VACANCY: Vice President"]
    )
    
    tester.run_test(
        "BBT020",
        "President cannot quit",
        ["President1", "QUIT President1", "EXIT"],
        ["President cannot quit", "Error"]
    )
    
    tester.run_test(
        "BBT021",
        "Cannot quit non-existent employee",
        ["President1", "QUIT Ghost", "EXIT"],
        ["does not exist", "Error"]
    )
    
    tester.run_test(
        "BBT021A",
        "BUG: When employee quits, subordinates disappear from display but remain in system",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "QUIT VP1",  # VP1 quits - should create vacancy, S1 and W1 should still appear
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "Supervisor: S1", "Worker: W1"]  # BUG: S1 and W1 likely won't show
    )
    
    tester.run_test(
        "BBT021B",
        "BUG: Subordinates of quitter still in lookup but not visible",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "QUIT VP1",
         "FIRE President1 S1",  # If S1 still exists, this should work or fail appropriately
         "EXIT"],
        ["S1"]  # Should mention S1 in some way (removed, does not exist, etc.)
    )
    
    tester.run_test(
        "BBT021C",
        "BUG: Fire also causes subordinates to disappear from display",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "FIRE President1 VP1",  # Fire VP1 - should show vacancy with S1 beneath
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "Supervisor: S1", "Worker: W1"]  # All should be visible
    )
    
    tester.run_test(
        "BBT021D",
        "BUG: Names are case sensitive causing duplicate issues",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 vp1",  # Different case - should be rejected as duplicate
         "EXIT"],
        ["already exists", "Error"]  # Should reject case-insensitive duplicates
    )
    
    tester.run_test(
        "BBT021E",
        "BUG: Case sensitive names - Bob and bob treated as different people",
        ["President1",
         "HIRE President1 Bob",
         "HIRE President1 bob",  # Should fail - same name different case
         "DISPLAY",
         "EXIT"],
        ["Error"]  # Should reject, not allow both Bob and bob
    )
    
    # ========== LAYOFF TESTS ==========
    
    tester.run_test(
        "BBT022",
        "Layoff with no opening removes employee",
        ["President1", "HIRE President1 VP1", "HIRE President1 VP2",
         "LAYOFF President1 VP1", "EXIT"],
        ["No comparable openings", "removed"]
    )
    
    tester.run_test(
        "BBT023",
        "Layoff worker moves to opening in same supervisor group",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1",
         "HIRE S1 W1", "HIRE S1 W2", "HIRE S1 W3",
         "FIRE S1 W3", "HIRE S1 W4",
         "LAYOFF S1 W1", "DISPLAY", "EXIT"],
        ["Successfully placed"]
    )
    
    tester.run_test(
        "BBT024",
        "Cannot layoff president",
        ["President1", "LAYOFF President1 President1", "EXIT"],
        ["Cannot lay off the President", "Error"]
    )
    
    tester.run_test(
        "BBT024A",
        "BUG: Layoff causes subordinates to disappear like quit/fire",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "LAYOFF VP1 S1",  # Layoff S1 - W1 and W2 should still be visible under vacancy
         "DISPLAY",
         "EXIT"],
        ["Worker: W1", "Worker: W2"]  # Workers should still be visible
    )
    
    # ========== TRANSFER TESTS ==========
    
    tester.run_test(
        "BBT025",
        "President can transfer across VPs",
        ["President1", "HIRE President1 VP1", "HIRE President1 VP2",
         "HIRE VP1 S1", "HIRE VP2 S2",
         "TRANSFER President1 S1 VP2", "DISPLAY", "EXIT"],
        ["Successfully placed"]
    )
    
    tester.run_test(
        "BBT026",
        "VP can transfer within own hierarchy",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1", "HIRE VP1 S2",
         "HIRE S1 W1", "TRANSFER VP1 W1 S2", "EXIT"],
        ["Successfully placed"]
    )
    
    tester.run_test(
        "BBT027",
        "Supervisor cannot transfer",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1", "HIRE VP1 S2",
         "HIRE S1 W1", "TRANSFER S1 W1 S2", "EXIT"],
        ["does not have permission", "Error"]
    )
    
    tester.run_test(
        "BBT028",
        "Cannot transfer to full position",
        ["President1", "HIRE President1 VP1", "HIRE President1 VP2",
         "HIRE VP1 S1", "HIRE VP1 S2", "HIRE VP1 S3",
         "HIRE VP2 S4",
         "TRANSFER President1 S4 VP1", "EXIT"],
        ["maximum direct reports", "Error"]
    )
    
    # ========== PROMOTE TESTS ==========
    
    tester.run_test(
        "BBT029",
        "Promote worker to supervisor (one level)",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1", "HIRE S1 W1",
         "PROMOTE VP1 W1", "DISPLAY", "EXIT"],
        ["Successfully promoted", "Supervisor: W1"]
    )
    
    tester.run_test(
        "BBT030",
        "Promote supervisor to VP (one level)",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1",
         "PROMOTE President1 S1", "DISPLAY", "EXIT"],
        ["Successfully promoted", "Vice President: S1"]
    )
    
    tester.run_test(
        "BBT031",
        "Cannot promote worker to VP (two levels)",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1", "HIRE S1 W1",
         "PROMOTE President1 W1", "EXIT"],
        ["can only be one level", "Error"]
    )
    
    tester.run_test(
        "BBT032",
        "Cannot promote VP further",
        ["President1", "HIRE President1 VP1",
         "PROMOTE President1 VP1", "EXIT"],
        ["cannot be promoted further", "Error"]
    )
    
    tester.run_test(
        "BBT033",
        "Cannot promote without vacancy",
        ["President1", "HIRE President1 VP1",
         "HIRE VP1 S1", "HIRE VP1 S2", "HIRE VP1 S3",
         "HIRE S1 W1",
         "PROMOTE VP1 W1", "EXIT"],
        ["maximum direct reports", "Error"]
    )
    
    tester.run_test(
        "BBT034",
        "Worker/Supervisor cannot be receiving manager for promotion",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1", "HIRE S1 W1",
         "PROMOTE S1 W1", "EXIT"],
        ["cannot promote", "Error"]
    )
    
    # ========== DISPLAY TESTS ==========
    
    tester.run_test(
        "BBT035",
        "Display shows complete hierarchy",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1", "HIRE S1 W1",
         "DISPLAY", "EXIT"],
        ["President: President1", "Vice President: VP1", 
         "Supervisor: S1", "Worker: W1"],
        should_contain_all=True
    )
    
    tester.run_test(
        "BBT036",
        "Display shows vacancies for supervisory positions",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1",
         "FIRE President1 VP1", "DISPLAY", "EXIT"],
        ["VACANCY: Vice President"]
    )
    
    tester.run_test(
        "BBT037",
        "Display does not show worker vacancies",
        ["President1", "HIRE President1 VP1", "HIRE VP1 S1",
         "HIRE S1 W1", "HIRE S1 W2",
         "DISPLAY", "EXIT"],
        ["Worker: W1", "Worker: W2"]
    )
    
    # ========== EDGE CASES ==========
    
    tester.run_test(
        "BBT038",
        "Fill vacancy after fire",
        ["President1", "HIRE President1 VP1", "FIRE President1 VP1",
         "HIRE President1 VP2", "DISPLAY", "EXIT"],
        ["Vice President: VP2", "Successfully placed"]
    )
    
    tester.run_test(
        "BBT039",
        "Complex scenario - multiple operations",
        ["President1", 
         "HIRE President1 VP1", 
         "HIRE VP1 S1", 
         "HIRE S1 W1",
         "HIRE S1 W2",
         "QUIT W1",
         "PROMOTE VP1 W2",
         "DISPLAY", 
         "EXIT"],
        ["President: President1", "Supervisor: W2"]
    )
    
    tester.run_test(
        "BBT040",
        "Case insensitivity of commands",
        ["President1", "hire President1 VP1", "display", "exit"],
        ["Vice President: VP1"]
    )
    
    # ========== BUG VERIFICATION TESTS ==========
    
    tester.run_test(
        "BBT041",
        "BUG: Unlimited promotions beyond VP - should stop at VP",
        ["President1", 
         "HIRE President1 VP1", 
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "PROMOTE VP1 W1",  # Worker -> Supervisor
         "PROMOTE President1 W1",  # Supervisor -> VP
         "PROMOTE President1 W1",  # Should FAIL - already VP
         "EXIT"],
        ["cannot be promoted further", "Error"]
    )
    
    tester.run_test(
        "BBT042",
        "BUG: VP can promote Supervisor to VP creating VP under VP (INVALID HIERARCHY)",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP2 S1",
         "PROMOTE VP1 S1",
         "DISPLAY",
         "EXIT"],
        ["Error", "cannot promote"]  # Should reject - VP can't promote to create VP under VP
    )
    
    tester.run_test(
        "BBT043",
        "BUG: Can create unlimited VP levels through repeated promotions",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "PROMOTE VP1 W1",
         "PROMOTE VP1 W1",  # Should fail - creates VP under VP
         "EXIT"],
        [("Error", "cannot")]  # Should reject nested VP structure
    )
    
    tester.run_test(
        "BBT043A",
        "BUG: Promotions can create 3+ vice presidents exceeding capacity",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",  # President at capacity (2 VPs)
         "HIRE VP1 S1",
         "PROMOTE President1 S1",  # S1 promoted to VP - should fail, president full
         "DISPLAY",
         "EXIT"],
        ["Error", "maximum"]  # Should fail - President can only have 2 VPs
    )
    
    tester.run_test(
        "BBT044",
        "VERIFY: Promoted employee gets correct capacity limits",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "PROMOTE President1 S1",  # S1 becomes VP (capacity should change to 3)
         "HIRE S1 X1",
         "HIRE S1 X2", 
         "HIRE S1 X3",
         "HIRE S1 X4",  # Should fail - VP can only have 3 supervisors
         "EXIT"],
        ["maximum direct reports", "Error"]  # Correctly enforces new capacity
    )
    
    # Print summary
    tester.print_summary()
    
    # Return exit code based on results
    return 0 if tester.failed == 0 else 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
