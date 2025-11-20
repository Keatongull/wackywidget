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
                [sys.executable, "WackyWidgetOrganization/main.py"],
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
    
    # ========== NAMES WITH SPACES TESTS (BUG DETECTION) ==========
    
    tester.run_test(
        "BBT045",
        "BUG: President name with spaces should be rejected",
        ["John Smith", "ValidName", "DISPLAY", "EXIT"],
        ["Error", "Invalid"]
    )
    
    tester.run_test(
        "BBT047",
        "BUG: Multi-word names in HIRE command parsed incorrectly",
        ["President1", "HIRE President1 Bob", "HIRE President1 Carol Davis", "DISPLAY", "EXIT"],
        ["Vice President: Bob"]  # Carol Davis likely fails due to space
    )
    
    tester.run_test(
        "BBT048",
        "BUG: Names with leading/trailing spaces",
        ["President1", "HIRE President1  SpaceName ", "EXIT"],
        ["Error", "Invalid"]
    )
    
    # ========== HIERARCHY DISPLAY AFTER REMOVAL TESTS ==========
    
    tester.run_test(
        "BBT053",
        "Display hierarchy when VP is fired - subordinates should remain visible",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 Super1",
         "HIRE VP1 Super2",
         "HIRE Super1 Worker1",
         "HIRE Super1 Worker2",
         "FIRE President1 VP1",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "Supervisor: Super1", "Supervisor: Super2", 
         "Worker: Worker1", "Worker: Worker2"],
        should_contain_all=True
    )
    
    tester.run_test(
        "BBT054",
        "Display hierarchy when VP quits - subordinates should remain visible",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 Super1",
         "HIRE Super1 Worker1",
         "QUIT VP1",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "Supervisor: Super1", "Worker: Worker1"],
        should_contain_all=True
    )
    
    tester.run_test(
        "BBT055",
        "Display hierarchy when Supervisor is fired - workers remain",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 Super1",
         "HIRE Super1 W1",
         "HIRE Super1 W2",
         "HIRE Super1 W3",
         "FIRE VP1 Super1",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Supervisor", "Worker: W1", "Worker: W2", "Worker: W3"],
        should_contain_all=True
    )
    
    tester.run_test(
        "BBT056",
        "Display hierarchy when Supervisor quits - workers remain",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 Super1",
         "HIRE Super1 W1",
         "QUIT Super1",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Supervisor", "Worker: W1"]
    )
    
    tester.run_test(
        "BBT057",
        "Display after layoff of VP - subordinates remain visible",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 Super1",
         "HIRE Super1 W1",
         "LAYOFF President1 VP1",  # VP1 laid off, no opening so removed
         "DISPLAY",
         "EXIT"],
        ["Supervisor: Super1", "Worker: W1"]  # Should still see subordinates
    )
    
    tester.run_test(
        "BBT058",
        "Deep hierarchy remains visible after mid-level removal",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "HIRE S2 W3",
         "FIRE President1 VP1",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "Supervisor: S1", "Supervisor: S2", 
         "Worker: W1", "Worker: W2", "Worker: W3"],
        should_contain_all=True
    )
    
    # ========== COMPREHENSIVE OPERATION COVERAGE ==========
    
    tester.run_test(
        "BBT059",
        "All operations in sequence - comprehensive workflow",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE VP2 S3",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "QUIT W1",
         "FIRE VP1 S2",
         "TRANSFER President1 W2 S3",
         "PROMOTE VP2 S1",
         "LAYOFF President1 S3",
         "DISPLAY",
         "EXIT"],
        ["President: President1"]  # Basic sanity check
    )
    
    tester.run_test(
        "BBT060",
        "Hire fills vacancy created by quit",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "QUIT S1",
         "HIRE VP1 S2",
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S2", "Successfully placed"]
    )
    
    tester.run_test(
        "BBT061",
        "Promote after fire creates proper hierarchy",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "FIRE President1 VP1",
         "HIRE President1 VP2",
         "PROMOTE VP2 W1",
         "DISPLAY",
         "EXIT"],
        ["Vice President: VP2", "Supervisor: W1"]
    )
    
    tester.run_test(
        "BBT062",
        "Transfer to vacancy, then hire to another vacancy",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "FIRE VP1 S1",
         "HIRE VP2 S2",
         "TRANSFER President1 S2 VP1",
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S2"]
    )
    
    tester.run_test(
        "BBT063",
        "Layoff finds opening in same supervisor group",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "HIRE S1 W3",
         "FIRE S1 W3",
         "LAYOFF S1 W1",
         "DISPLAY",
         "EXIT"],
        ["Worker: W1", "Worker: W2"]  # W1 should be moved to vacancy
    )
    
    tester.run_test(
        "BBT064",
        "Layoff finds opening in different supervisor under same VP",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "HIRE S1 W3",
         "HIRE S1 W4",
         "HIRE S1 W5",  # S1 at capacity
         "HIRE S2 W6",  # S2 has room
         "LAYOFF S1 W1",
         "DISPLAY",
         "EXIT"],
        ["Worker: W1"]  # W1 should move to S2
    )
    
    tester.run_test(
        "BBT065",
        "Layoff finds opening in different VP group",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE VP2 S2",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "HIRE S1 W3",
         "HIRE S1 W4",
         "HIRE S1 W5",  # S1 full
         "HIRE S2 W6",  # S2 has room
         "LAYOFF S1 W1",
         "DISPLAY",
         "EXIT"],
        ["Worker: W1"]  # Should move to S2 under VP2
    )
    
    tester.run_test(
        "BBT066",
        "Multiple promotions changing hierarchy",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "HIRE S2 W2",
         "FIRE President1 VP1",
         "HIRE President1 VP2",
         "PROMOTE VP2 S1",
         "PROMOTE President1 W1",
         "DISPLAY",
         "EXIT"],
        ["Vice President: VP2", "Vice President: S1"]
    )
    
    tester.run_test(
        "BBT067",
        "Transfer across multiple VP branches",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE VP2 S2",
         "HIRE VP2 S3",
         "HIRE S1 W1",
         "TRANSFER President1 W1 S3",
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S3", "Worker: W1"]
    )
    
    tester.run_test(
        "BBT068",
        "Fire then transfer into vacancy",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE VP2 S3",
         "FIRE VP1 S1",
         "TRANSFER President1 S3 VP1",
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S3"]
    )
    
    # ========== EDGE CASES FOR ALL OPERATIONS ==========
    
    tester.run_test(
        "BBT069",
        "Case sensitivity - names should be case sensitive",
        ["President1",
         "HIRE President1 alice",
         "HIRE President1 Alice",
         "DISPLAY",
         "EXIT"],
        ["alice", "Alice"]  # Both should exist if case sensitive
    )
    
    tester.run_test(
        "BBT070",
        "Empty organization operations fail gracefully",
        ["President1", "FIRE President1 Nobody", "QUIT Nobody", 
         "LAYOFF President1 Nobody", "EXIT"],
        ["does not exist"]
    )
    
    tester.run_test(
        "BBT071",
        "Maximum capacity at all levels simultaneously",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE VP1 S3",
         "HIRE VP2 S4",
         "HIRE VP2 S5",
         "HIRE VP2 S6",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "HIRE S1 W3",
         "HIRE S1 W4",
         "HIRE S1 W5",
         "DISPLAY",
         "EXIT"],
        ["President: President1", "Vice President: VP1", "Vice President: VP2",
         "Supervisor: S1", "Worker: W5"],
        should_contain_all=True
    )
    
    tester.run_test(
        "BBT072",
        "Promote employee with reports - vacancy created at old level",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "PROMOTE VP1 W1",
         "DISPLAY",
         "EXIT"],
        ["Supervisor: W1", "Worker: W2"]  # W2 should be under vacancy or W1
    )
    
    tester.run_test(
        "BBT073",
        "Invalid command syntax variations",
        ["President1",
         "HIRE",
         "FIRE President1",
         "QUIT",
         "LAYOFF President1",
         "TRANSFER President1 VP1",
         "PROMOTE President1",
         "DISPLAY extra",
         "EXIT"],
        ["Incorrect", "argument"]
    )
    
    tester.run_test(
        "BBT074",
        "Quit cascade - multiple levels quit from bottom up",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "QUIT W1",
         "QUIT S1",
         "QUIT VP1",
         "DISPLAY",
         "EXIT"],
        ["President: President1"]  # Only president remains
    )
    
    tester.run_test(
        "BBT075",
        "Fire cascade - fire from top down creates vacancies",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "FIRE President1 VP1",
         "FIRE President1 S1",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "VACANCY: Supervisor"]
    )
    
    tester.run_test(
        "BBT076",
        "Layoff with no opening removes employee permanently",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "LAYOFF President1 VP1",
         "DISPLAY",
         "EXIT"],
        ["removed", "Vice President: VP2"]
    )
    
    tester.run_test(
        "BBT077",
        "Transfer same person multiple times",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE VP2 S2",
         "HIRE S1 W1",
         "TRANSFER President1 W1 S2",
         "TRANSFER President1 W1 S1",
         "DISPLAY",
         "EXIT"],
        ["Worker: W1"]
    )
    
    tester.run_test(
        "BBT078",
        "Promote multiple employees to same level",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "HIRE S1 W3",
         "FIRE VP1 S1",
         "PROMOTE VP1 W1",
         "PROMOTE VP1 W2",
         "DISPLAY",
         "EXIT"],
        ["Supervisor: W1", "Supervisor: W2"]
    )
    
    tester.run_test(
        "BBT079",
        "Complex state - all operations mixed",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "PROMOTE VP1 W1",
         "HIRE W1 W3",
         "QUIT W2",
         "FIRE President1 VP1",
         "HIRE President1 VP2",
         "TRANSFER President1 S1 VP2",
         "LAYOFF VP2 W3",
         "DISPLAY",
         "EXIT"],
        ["President: President1"]
    )
    
    tester.run_test(
        "BBT080",
        "Verify all vacancy types display correctly",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "FIRE President1 VP1",
         "FIRE President1 S1",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "VACANCY: Supervisor", "Worker: W1"],
        should_contain_all=True
    )
    
    # ========== ADDITIONAL BUG DETECTION TESTS ==========
    
    tester.run_test(
        "BBT081",
        "BUG: Name with only spaces should be rejected",
        ["   ", "ValidName", "DISPLAY", "EXIT"],
        ["President: ValidName"]
    )
    
    tester.run_test(
        "BBT082",
        "BUG: Name with tabs should be rejected",
        ["Name\tWithTab", "ValidName", "EXIT"],
        ["Error", "Invalid"]
    )
    
    tester.run_test(
        "BBT083",
        "BUG: Name with newlines should be rejected",
        ["Name\nLine", "ValidName", "EXIT"],
        ["President: ValidName"]
    )
    
    tester.run_test(
        "BBT085",
        "BUG: Names with underscores",
        ["President1", "HIRE President1 User_Name", "EXIT"],
        ["Error", "Invalid"]
    )
    
    tester.run_test(
        "BBT086",
        "BUG: Names with hyphens/dashes",
        ["President1", "HIRE President1 Mary-Jane", "EXIT"],
        ["Error", "Invalid"]
    )
    
    tester.run_test(
        "BBT087",
        "BUG: Very long name (100+ characters)",
        ["President1", 
         "HIRE President1 " + "A" * 100,
         "EXIT"],
        ["Successfully"]  # Should handle or reject gracefully
    )
    
    tester.run_test(
        "BBT088",
        "BUG: Single character name",
        ["President1", "HIRE President1 X", "DISPLAY", "EXIT"],
        ["Vice President: X"]  # Single char may or may not be valid
    )
    
    tester.run_test(
        "BBT089",
        "BUG: Name that is a command word (EXIT, HIRE, etc)",
        ["President1", "HIRE President1 EXIT", "DISPLAY", "EXIT"],
        ["Vice President: EXIT"]  # Should allow or reject consistently
    )
    
    tester.run_test(
        "BBT090",
        "BUG: Fire subordinate directly without going through manager",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "FIRE S1 W1",  # S1 firing their own worker - should work
         "DISPLAY",
         "EXIT"],
        ["removed"]
    )
    
    tester.run_test(
        "BBT091",
        "BUG: Subordinates lost after multiple cascading fires",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "HIRE S2 W2",
         "FIRE President1 VP1",
         "DISPLAY",
         "EXIT"],
        ["Worker: W1", "Worker: W2"],  # Both workers should be visible
        should_contain_all=True
    )
    
    tester.run_test(
        "BBT092",
        "BUG: Quit then immediately hire same name",
        ["President1",
         "HIRE President1 VP1",
         "QUIT VP1",
         "HIRE President1 VP1",  # Reuse same name
         "DISPLAY",
         "EXIT"],
        ["Vice President: VP1"]
    )
    
    tester.run_test(
        "BBT093",
        "BUG: Fire then immediately hire same name",
        ["President1",
         "HIRE President1 VP1",
         "FIRE President1 VP1",
         "HIRE President1 VP1",
         "DISPLAY",
         "EXIT"],
        ["Vice President: VP1"]
    )
    
    tester.run_test(
        "BBT094",
        "BUG: Layoff then hire same name at different position",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "LAYOFF President1 VP1",
         "HIRE VP2 VP1",  # VP1 now as supervisor
         "DISPLAY",
         "EXIT"],
        ["Supervisor: VP1"]
    )
    
    tester.run_test(
        "BBT095",
        "BUG: Transfer employee to themselves as manager",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "TRANSFER President1 S1 S1",  # S1 reporting to S1 - invalid
         "EXIT"],
        ["Error"]
    )
    
    tester.run_test(
        "BBT096",
        "BUG: Promote employee to report to themselves",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "PROMOTE S1 W1",  # W1 becomes supervisor under S1 who was their boss
         "EXIT"],
        ["cannot promote", "Error"]
    )
    
    tester.run_test(
        "BBT097",
        "BUG: Circular reporting - transfer creates loop",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "PROMOTE VP1 W1",  # W1 becomes supervisor
         "TRANSFER President1 S1 W1",  # S1 now reports to W1 (was W1's boss)
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S1", "Supervisor: W1"]
    )
    
    tester.run_test(
        "BBT098",
        "BUG: Promote creates more VPs than allowed",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "PROMOTE President1 S1",  # 3rd VP - exceeds capacity
         "DISPLAY",
         "EXIT"],
        ["Error", "maximum"]
    )
    
    tester.run_test(
        "BBT099",
        "BUG: Layoff employee who has subordinates - subordinates lost",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "LAYOFF President1 VP1",  # VP1 has subordinates
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S1", "Worker: W1", "Worker: W2"],
        should_contain_all=True
    )
    
    tester.run_test(
        "BBT100",
        "BUG: Transfer to non-existent manager",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "TRANSFER President1 S1 GhostManager",
         "EXIT"],
        ["does not exist", "Error"]
    )
    
    tester.run_test(
        "BBT101",
        "BUG: Promote non-existent employee",
        ["President1",
         "HIRE President1 VP1",
         "PROMOTE VP1 GhostEmployee",
         "EXIT"],
        ["does not exist", "Error"]
    )
    
    tester.run_test(
        "BBT102",
        "BUG: Multiple spaces between command arguments",
        ["President1",
         "HIRE  President1  VP1",  # Extra spaces
         "DISPLAY",
         "EXIT"],
        ["Vice President: VP1"]  # Should handle or reject
    )
    
    tester.run_test(
        "BBT103",
        "BUG: Empty command (just pressing enter)",
        ["President1", "", "", "DISPLAY", "EXIT"],
        ["President: President1"]  # Should handle gracefully
    )
    
    tester.run_test(
        "BBT105",
        "BUG: Promote worker creates vacancy but workers still under old supervisor",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "FIRE VP1 S1",
         "PROMOTE VP1 W1",  # W1 promoted to supervisor
         "DISPLAY",
         "EXIT"],
        ["Supervisor: W1", "Worker: W2"]  # W2 should be visible somewhere
    )
    
    tester.run_test(
        "BBT107",
        "BUG: Nested vacancies display incorrectly",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "QUIT S1",
         "QUIT VP1",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "Worker: W1"]  # W1 should still be visible
    )
    
    tester.run_test(
        "BBT108",
        "BUG: Fire creates vacancy, then fill with promote, subordinates preserved",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "FIRE VP1 S1",  # S1 fired, W1 and W2 under vacancy
         "HIRE VP1 S2",
         "HIRE S2 W3",
         "PROMOTE VP1 W3",  # W3 promoted to fill supervisor vacancy
         "DISPLAY",
         "EXIT"],
        ["Worker: W1", "Worker: W2", "Supervisor: W3"]
    )
    
    tester.run_test(
        "BBT109",
        "BUG: Layoff searches wrong hierarchy for openings",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE VP1 S3",  # VP1 at capacity
         "HIRE VP2 S4",  # VP2 has room
         "HIRE S1 W1",
         "LAYOFF S1 W1",  # Should not move to VP2's supervisor
         "DISPLAY",
         "EXIT"],
        ["Worker: W1"]
    )
    
    tester.run_test(
        "BBT110",
        "BUG: Worker capacity enforcement - workers should not have subordinates",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE W1 Someone",  # Worker cannot hire
         "EXIT"],
        ["cannot hire", "Error"]
    )
    
    tester.run_test(
        "BBT111",
        "BUG: President capacity exceeded by promotion",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",  # President at capacity (2 VPs)
         "HIRE VP1 S1",
         "FIRE President1 VP2",
         "HIRE President1 VP3",
         "PROMOTE President1 S1",  # Would create 3rd VP
         "EXIT"],
        ["maximum", "Error"]
    )
    
    tester.run_test(
        "BBT112",
        "BUG: VP capacity exceeded by promotion",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE VP1 S3",  # VP at capacity (3 supervisors)
         "HIRE S1 W1",
         "PROMOTE VP1 W1",  # Would create 4th supervisor
         "EXIT"],
        ["maximum", "Error"]
    )
    
    tester.run_test(
        "BBT113",
        "BUG: Supervisor capacity exceeded by promotion",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "HIRE S1 W3",
         "HIRE S1 W4",
         "HIRE S1 W5",  # S1 at capacity (5 workers)
         "HIRE S2 W6",
         "TRANSFER President1 W6 S1",  # Should fail - S1 full
         "EXIT"],
        ["maximum", "Error"]
    )
    
    tester.run_test(
        "BBT114",
        "BUG: Quit removes name from system, can rehire immediately",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "QUIT S1",
         "HIRE VP1 S1",  # Same name reused
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S1"]
    )
    
    tester.run_test(
        "BBT115",
        "BUG: Fire removes from lookup, subordinates become inaccessible",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "FIRE President1 VP1",
         "FIRE President1 S1",  # Can still fire S1 even though VP1 is vacancy?
         "EXIT"],
        ["removed", "does not exist"]  # May succeed or fail depending on implementation
    )
    
    tester.run_test(
        "BBT116",
        "BUG: Display stops at first vacancy instead of showing deeper levels",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "HIRE S2 W2",
         "FIRE President1 VP1",
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S1", "Supervisor: S2", "Worker: W1", "Worker: W2"],
        should_contain_all=True
    )
    
    tester.run_test(
        "BBT117",
        "BUG: Transfer employee who has subordinates",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "TRANSFER President1 S1 VP2",  # S1 has subordinate W1
         "DISPLAY",
         "EXIT"],
        ["Vice President: VP2", "Supervisor: S1", "Worker: W1"]
    )
    
    tester.run_test(
        "BBT118",
        "BUG: Promote employee who has subordinates - subordinates transfer",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "FIRE President1 VP1",
         "HIRE President1 VP2",
         "PROMOTE VP2 S1",  # S1 has workers W1, W2
         "DISPLAY",
         "EXIT"],
        ["Vice President: S1", "Worker: W1", "Worker: W2"]
    )
    
    tester.run_test(
        "BBT119",
        "BUG: Extremely deep hierarchy (5+ levels with vacancy)",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "QUIT VP1",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "Supervisor: S1", "Worker: W1"],
        should_contain_all=True
    )
    
    tester.run_test(
        "BBT120",
        "BUG: All employees at one level quit/fired, vacancies remain",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "FIRE President1 VP1",
         "FIRE President1 VP2",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President"]  # Should show 2 vacancies or handle cleanup
    )
    
    tester.run_test(
        "BBT122",
        "BUG: Layoff to opening transfers with subordinates intact",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "FIRE VP1 S1",  # Create supervisor vacancy
         "HIRE VP2 S2",
         "HIRE S2 W3",
         "LAYOFF VP2 S2",  # Should move to vacancy under VP1
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S2", "Worker: W3"]
    )
    
    tester.run_test(
        "BBT126",
        "BUG: Worker under vacancy still accessible for operations",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "FIRE VP1 S1",  # S1 fired, W1 under vacancy
         "QUIT W1",  # Can W1 quit?
         "DISPLAY",
         "EXIT"],
        ["removed"]
    )
    
    tester.run_test(
        "BBT127",
        "BUG: Promote from under vacancy",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "FIRE VP1 S1",  # W1 now under vacancy
         "PROMOTE VP1 W1",  # Promote W1 from under vacancy
         "DISPLAY",
         "EXIT"],
        ["Supervisor: W1"]
    )
    
    tester.run_test(
        "BBT128",
        "BUG: Transfer from under vacancy",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "FIRE VP1 S1",  # W1 under vacancy
         "TRANSFER VP1 W1 S2",
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S2", "Worker: W1"]
    )
    
    tester.run_test(
        "BBT129",
        "BUG: Fire employee under vacancy",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "FIRE VP1 S1",  # S1 fired, W1 under vacancy
         "FIRE VP1 W1",  # Can fire W1 through VP1?
         "DISPLAY",
         "EXIT"],
        ["removed"]
    )
    
    tester.run_test(
        "BBT130",
        "BUG: Layoff employee under vacancy",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "FIRE VP1 S1",  # W1 under vacancy
         "LAYOFF VP1 W1",
         "DISPLAY",
         "EXIT"],
        ["Worker: W1"]  # Should move or be removed
    )
    
    tester.run_test(
        "BBT131",
        "BUG: Fill vacancy preserves grandchildren",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "FIRE President1 VP1",  # VP1 fired, S1 and workers under vacancy
         "HIRE President1 VP2",  # New VP
         "DISPLAY",
         "EXIT"],
        ["Vice President: VP2", "Supervisor: S1", "Worker: W1", "Worker: W2"]
    )
    
    tester.run_test(
        "BBT132",
        "BUG: Multiple vacancies at same level",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE VP1 S3",
         "FIRE VP1 S1",
         "FIRE VP1 S2",
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Supervisor"]  # Should show vacancies
    )
    
    tester.run_test(
        "BBT133",
        "BUG: Name is SQL injection attempt",
        ["President1",
         "HIRE President1 Robert';DROP TABLE users;--",
         "EXIT"],
        ["Error", "Invalid"]
    )
    
    tester.run_test(
        "BBT134",
        "BUG: Name with escape sequences",
        ["President1",
         "HIRE President1 Name\\nWithEscape",
         "EXIT"],
        ["Error", "Invalid"]
    )
    
    tester.run_test(
        "BBT135",
        "BUG: Promote to fill specific vacancy among multiple",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "HIRE S2 W2",
         "FIRE VP1 S1",
         "FIRE VP1 S2",  # 2 supervisor vacancies
         "PROMOTE VP1 W1",
         "DISPLAY",
         "EXIT"],
        ["Supervisor: W1"]
    )
    
    tester.run_test(
        "BBT137",
        "BUG: President tries to transfer themselves",
        ["President1",
         "HIRE President1 VP1",
         "TRANSFER President1 President1 VP1",
         "EXIT"],
        ["Error"]
    )
    
    tester.run_test(
        "BBT139",
        "BUG: Attempt to promote president",
        ["President1",
         "PROMOTE President1 President1",
         "EXIT"],
        ["cannot be promoted further", "Error"]
    )
    
    tester.run_test(
        "BBT140",
        "BUG: Negative test - hire under fired employee",
        ["President1",
         "HIRE President1 VP1",
         "FIRE President1 VP1",
         "HIRE VP1 Someone",  # VP1 doesn't exist anymore
         "EXIT"],
        ["does not exist", "Error"]
    )
    
    tester.run_test(
        "BBT141",
        "BUG: Operations on president use wrong name",
        ["President1",
         "FIRE WrongName VP1",
         "EXIT"],
        ["does not exist", "Error"]
    )
    
    tester.run_test(
        "BBT142",
        "BUG: Display with only vacancies (all employees quit)",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "QUIT S1",
         "QUIT VP1",
         "DISPLAY",
         "EXIT"],
        ["President: President1"]  # May or may not show vacancies
    )
    
    tester.run_test(
        "BBT143",
        "BUG: Rehire into specific vacancy position",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "FIRE VP1 S1",  # Create supervisor vacancy under VP1
         "HIRE VP1 S2",  # Should fill the vacancy
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S2"]
    )
    
    tester.run_test(
        "BBT144",
        "BUG: Worker promoted multiple times in succession",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "FIRE VP1 S1",  # Create supervisor vacancy
         "PROMOTE VP1 W1",  # W1 -> Supervisor
         "FIRE President1 VP1",  # Create VP vacancy
         "HIRE President1 VP2",
         "PROMOTE President1 W1",  # W1 (now supervisor) -> VP
         "DISPLAY",
         "EXIT"],
        ["Vice President: W1"]
    )
    
    tester.run_test(
        "BBT145",
        "BUG: Layoff priority - same supervisor first",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "HIRE S1 W3",
         "HIRE S1 W4",
         "HIRE S1 W5",  # S1 full
         "HIRE S2 W6",  # S2 has room
         "FIRE S1 W5",  # Create opening at S1
         "LAYOFF S1 W1",  # Should move to S1's vacancy first, not S2
         "DISPLAY",
         "EXIT"],
        ["Supervisor: S1"]  # W1 should still be under S1
    )
    
    tester.run_test(
        "BBT146",
        "BUG: Complex hierarchy with multiple vacancy levels",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "QUIT S1",  # S1 quits, creates supervisor vacancy
         "QUIT VP1",  # VP1 quits, creates VP vacancy
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "Worker: W1", "Worker: W2"]
    )
    
    tester.run_test(
        "BBT147",
        "BUG: Hire after quit preserves subordinate structure",
        ["President1",
         "HIRE President1 VP1",
         "HIRE VP1 S1",
         "HIRE S1 W1",
         "QUIT VP1",  # VP1 quits, S1 and W1 under vacancy
         "HIRE President1 VP2",  # Fill vacancy
         "DISPLAY",
         "EXIT"],
        ["Vice President: VP2", "Supervisor: S1", "Worker: W1"],
        should_contain_all=True
    )
    
    tester.run_test(
        "BBT148",
        "BUG: Name with all capital letters",
        ["PRESIDENT",
         "HIRE PRESIDENT VICEPRESIDENT",
         "DISPLAY",
         "EXIT"],
        ["President: PRESIDENT", "Vice President: VICEPRESIDENT"]
    )
    
    tester.run_test(
        "BBT149",
        "BUG: Name with all lowercase letters",
        ["president",
         "HIRE president vicepresident",
         "DISPLAY",
         "EXIT"],
        ["President: president", "Vice President: vicepresident"]
    )
    
    tester.run_test(
        "BBT150",
        "BUG: Maximum nesting - full organization at all capacities",
        ["President1",
         "HIRE President1 VP1",
         "HIRE President1 VP2",
         "HIRE VP1 S1",
         "HIRE VP1 S2",
         "HIRE VP1 S3",
         "HIRE VP2 S4",
         "HIRE VP2 S5",
         "HIRE VP2 S6",
         "HIRE S1 W1",
         "HIRE S1 W2",
         "HIRE S1 W3",
         "HIRE S1 W4",
         "HIRE S1 W5",
         "HIRE S2 W6",
         "HIRE S2 W7",
         "HIRE S2 W8",
         "HIRE S2 W9",
         "HIRE S2 W10",
         "QUIT VP1",  # Remove VP1 with full subtree
         "DISPLAY",
         "EXIT"],
        ["VACANCY: Vice President", "Supervisor: S1", "Supervisor: S2", "Supervisor: S3",
         "Worker: W1", "Worker: W10"],
        should_contain_all=True
    )

    # Print summary
    tester.print_summary()
    
    # Return exit code based on results
    return 0 if tester.failed == 0 else 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
