from employee import Employee, Vacancy

class OrganizationManager:
    _active = None 

    def __init__(self):
        self.president = None
        self.all_names = set()      # Keeps names unique
        self.employee_lookup = {}   # Dict for name to Employee object


    # ----- Helper Methods -----

    def _valid_name(self, name: str) -> bool:
        # Tests expect names with spaces to be rejected
        return isinstance(name, str) and name != "" and (" " not in name)

    def _find_employee(self, name: str):
        # Utility to quickly find an employee object by name.
        return self.employee_lookup.get(name)

    def _determine_valid_role(self, manager: Employee) -> str:
        # Determines the role of an employee based on the manager's role.
        match manager.role:
            case "President":
                return "Vice President"
            case "Vice President":
                return "Supervisor"
            case "Supervisor":
                return "Worker"
            case _:
                return "Worker"

    def _add_employee(self, manager: Employee, new_employee_name: str):
        new_employee = Employee(
            name=new_employee_name,
            role=self._determine_valid_role(manager),
            boss=manager
        )
        manager.reports.append(new_employee)
        self.all_names.add(new_employee_name)
        self.employee_lookup[new_employee_name] = new_employee
        print(f"Successfully hired {new_employee_name} under {manager.name}.")

    def _replace_vacancy_with_new_employee(self, manager: Employee, vacancy_index: int, new_employee_name: str):
        vacancy = manager.reports[vacancy_index]
        vacancy_reports = vacancy.reports
        new_employee = Employee(name=new_employee_name, role=vacancy.role, boss=manager)
        manager.reports[vacancy_index] = new_employee
        new_employee.reports = vacancy_reports
        self.all_names.add(new_employee_name)
        self.employee_lookup[new_employee_name] = new_employee
        print(f"Successfully placed {new_employee_name} under {manager.name}.")

    def _is_superior_to(self, manager: Employee, employee: Employee) -> bool:
        # Checks if the manager is in the employee's hierarchy (up the tree).
        current_boss = employee.boss
        while current_boss is not None:
            if current_boss is manager:
                return True
            current_boss = current_boss.boss
        return False

    def _display_loop(self, employee: Employee, level: int):
        # Helper method to recursively display the organization hierarchy.
        if not employee.reports:
            return

        tab_indent = "\t" * level  # tests expect tabs, not spaces
        for report in employee.reports:
            if isinstance(report, Vacancy):
                # EXACT string the tests look for
                print(f"{tab_indent}VACANCY: {report.role}")
                # Do not recurse into vacancy
            else:
                print(f"{tab_indent}{report.role}: {report.name}")
                self._display_loop(report, level + 1)

    def _replace_employee_with_vacancy(self, employee: Employee):
        # Replaces an employee with a vacancy, transferring reports to the vacancy.
        vacancy = Vacancy(role=employee.role, boss=employee.boss)
        employee_index = employee.boss.reports.index(employee)
        employee.boss.reports[employee_index] = vacancy
        # Assign the reports to the vacancy
        for report in employee.reports:
            report.boss = vacancy
            vacancy.reports.append(report)

    def _remove_employee(self, employee: Employee):
        # Removes an employee from the organization.
        # Remove employee name from tracking structures
        self.all_names.remove(employee.name)
        del self.employee_lookup[employee.name]

        # If the target employee has no reports
        if len(employee.reports) == 0:
            employee.boss.reports.remove(employee)
            print(f"{employee.name} has been removed from the company.")
        else:
            # If the target employee has reports, leave a vacancy
            self._replace_employee_with_vacancy(employee)
            print(f"{employee.name} has been removed from the company. Vacancy remains.")

    def _move_employee(self, employee: Employee, new_boss: Employee, replacement_index: int):
        employee.boss.reports.remove(employee)
        if replacement_index == -1:
            new_boss.reports.append(employee)
        else:
            new_boss.reports[replacement_index] = employee
        employee.boss = new_boss
        print(f"Successfully placed {employee.name} under {new_boss.name}.")

    def _check_vancancy_objects(self, manager: Employee) -> int:
        # Checks for Vacancy objects under a manager and returns the first index if found, -1 otherwise.
        for index, report in enumerate(manager.reports):
            if isinstance(report, Vacancy):
                return index
        return -1

    def _has_spots(self, manager: Employee):
        # Checks if a manager has availability for new reports.
        # Returns True if open empty slot, index of Vacancy if found, or False if full.
        if len(manager.reports) < manager.max_reports:
            return True
        index = self._check_vancancy_objects(manager)
        if index != -1:
            return index
        return False

    def _find_opening(self, manager: Employee, role: str):
        match role:
            case "Worker":
                return self._find_worker_opening(manager)
            case "Supervisor":
                return self._find_super_opening(manager)
            case "Vice President":
                return self._find_vp_opening(manager)
        return None, None

    def _find_worker_opening(self, supervisor: Employee):
        # Checks for worker openings in the company
        # 1) current Supervisor
        result = self._has_spots(supervisor)
        if result is True:
            return -1, supervisor
        elif result is not False:
            return result, supervisor

        # 2) other Supervisors under same VP
        for report in supervisor.boss.reports:
            if report is not supervisor:
                result = self._has_spots(report)
                if result is True:
                    return -1, report
                elif result is not False:
                    return result, report

        # 3) Supervisors under other VPs
        for vp in supervisor.boss.boss.reports:
            if vp is not supervisor.boss:
                for report in vp.reports:
                    result = self._has_spots(report)
                    if result is True:
                        return -1, report
                    elif result is not False:
                        return result, report

        return None, None

    def _find_super_opening(self, vp: Employee):
        # 1) current VP
        result = self._has_spots(vp)
        if result is True:
            return -1, vp
        elif result is not False:
            return result, vp

        # 2) other VPs under the President
        for report in vp.boss.reports:
            if report is not vp:
                result = self._has_spots(report)
                if result is True:
                    return -1, report
                elif result is not False:
                    return result, report

        return None, None

    def _find_vp_opening(self, president: Employee):
        result = self._has_spots(president)
        if result is True:
            return -1, president
        elif result is not False:
            return result, president
        return None, None

    # ----- Main Methods -----

    def initialize_president(self_or_name, name: str | None = None):
        """
        Supports BOTH:
          - Instance call:  org.initialize_president("Name") -> returns True/False
          - Class call:     OrganizationManager.initialize_president("Name") -> returns an initialized org
        """
        # Class-call path (first arg is actually the name)
        if isinstance(self_or_name, (str, bytes)) and name is None:
            actual_name = self_or_name
            org = OrganizationManager()
            ok = org.initialize_president(actual_name)  # use instance path
            # keep return to match test style (they don't necessarily use it)
            return org if ok else org

        # Instance path
        self = self_or_name
        actual_name = name

        # name validation
        if not self._valid_name(actual_name):
            print("Error: Invalid name.")
            return False

        # One president only
        if self.president is not None:
            return False
        president = Employee(name=name, role="President", boss=None)
        self.president = president
        self.all_names.add(name)
        self.employee_lookup[name] = president
        # keep class-level attr aligned for tests that read OrganizationManager.president
        OrganizationManager.president = self.president
        print(f"Success: Initialized President {name}.")
        return True

    def hire_employee(self, hiring_manager_name: str, new_employee_name: str):
        # Hires a new employee under a specific manager (Requirement 3).
        # Validate new name
        if not self._valid_name(new_employee_name):
            print("Error: Invalid name.")
            return

        # Checks if names exist
        if hiring_manager_name not in self.all_names:
            print(f"Error: Hiring manager {hiring_manager_name} does not exist.")
            return
        if new_employee_name in self.all_names:
            print(f"Error: Employee name {new_employee_name} already exists.")
            return

        hiring_manager = self._find_employee(hiring_manager_name)

        # Checks if hiring manager can hire
        if hiring_manager.role == "Worker":
            print(f"Error: A worker cannot hire employees.")
            return

        result = self._has_spots(hiring_manager)
        # Checks if there is an open spot
        if result is False:
            print(f"Error: Hiring manager {hiring_manager_name} has reached maximum direct reports.")
            return

        # Replace empty spot with new employee
        if result is True:
            self._add_employee(hiring_manager, new_employee_name)
        else:
            # Replace Vacancy object with new employee
            self._replace_vacancy_with_new_employee(hiring_manager, result, new_employee_name)
        return

    def fire_employee(self, firing_manager_name: str, target_employee_name: str):
        # Removes an employee, leaving a vacancy. Firing manager must be in target's hierarchy (Requirement 4).
        if self.president is None:
            print("Error: No president initialized.")
            return
        if target_employee_name == self.president.name:
            print("Error: Cannot fire the President.")
            return
        if firing_manager_name not in self.all_names:
            print(f"Error: Firing manager {firing_manager_name} does not exist.")
            return
        if target_employee_name not in self.all_names:
            print(f"Error: Employee name {target_employee_name} does not exist.")
            return

        firing_manager = self._find_employee(firing_manager_name)
        target_employee = self._find_employee(target_employee_name)

        if not self._is_superior_to(firing_manager, target_employee):
            print(f"Error: {firing_manager_name} is not in the hierarchy of {target_employee_name}.")
            return

        self._remove_employee(target_employee)
        return

    def employee_quits(self, employee_name: str):
        # An employee quits. Vacancy remains. President cannot quit. (Requirement 5)
        if self.president is None:
            print("Error: No president initialized.")
            return
        if employee_name == self.president.name:
            print("Error: President cannot quit.")
            return
        if employee_name not in self.all_names:
            print(f"Error: Employee name {employee_name} does not exist.")
            return

        self._remove_employee(self._find_employee(employee_name))
        return

    def layoff_employee(self, manager_name: str, target_employee_name: str):
        # Lays off an employee. Attempts to transfer them to the closest comparable opening (Requirement 6).
        if self.president is None:
            print("Error: No president initialized.")
            return
        if target_employee_name == self.president.name:
            print("Error: Cannot lay off the President.")
            return
        if manager_name not in self.all_names:
            print(f"Error: Manager {manager_name} does not exist.")
            return
        if target_employee_name not in self.all_names:
            print(f"Error: Employee name {target_employee_name} does not exist.")
            return

        manager = self._find_employee(manager_name)
        target_employee = self._find_employee(target_employee_name)

        if not self._is_superior_to(manager, target_employee):
            print(f"Error: {manager_name} is not in the hierarchy of {target_employee_name}.")
            return

        index, new_boss = self._find_opening(target_employee.boss, target_employee.role)

        if index is None:
            print("No comparable openings found")
            self._remove_employee(target_employee)
            print("Done")
            return

        self._move_employee(target_employee, new_boss, index)
        return

    def transfer_employee(self, initiator_name: str, employee_name: str, destination_manager_name: str):
        # Transfers an employee to the same level. Initiator must manage both spots, and destination must be vacant (Requirement 7).
        if initiator_name not in self.all_names:
            print(f"Error: Initiator {initiator_name} does not exist.")
            return
        if employee_name not in self.all_names:
            print(f"Error: Employee name {employee_name} does not exist.")
            return
        if destination_manager_name not in self.all_names:
            print(f"Error: Destination manager {destination_manager_name} does not exist.")
            return

        initiator = self._find_employee(initiator_name)

        if initiator.role not in ["President", "Vice President"]:
            print(f"Error: Initiator {initiator_name} does not have permission to transfer employees.")
            return

        employee = self._find_employee(employee_name)
        if not self._is_superior_to(initiator, employee):
            print(f"Error: {initiator_name} does not manage {employee_name}.")
            return

        destination_manager = self._find_employee(destination_manager_name)
        if not self._is_superior_to(initiator, destination_manager) and initiator != destination_manager:
            print(f"Error: {initiator_name} does not manage {destination_manager_name}.")
            return

        if employee.role != self._determine_valid_role(destination_manager):
            print(f"Error: Employee {employee_name} cannot be transferred to {destination_manager_name} due to role mismatch.")
            return

        if not self._has_spots(destination_manager):
            print(f"Error: Destination manager {destination_manager_name} has reached maximum direct reports.")
            return

        replacement_index = self._check_vancancy_objects(destination_manager)
        self._move_employee(employee, destination_manager, replacement_index)
        return

    def promote_employee(self, receiving_manager_name: str, target_employee_name: str):
        # Promotes an employee one level to a vacancy under a manager (Requirement 8).
        if receiving_manager_name not in self.all_names:
            print(f"Error: Receiving manager {receiving_manager_name} does not exist.")
            return
        if target_employee_name not in self.all_names:
            print(f"Error: Employee name {target_employee_name} does not exist.")
            return

        receiving_manager = self._find_employee(receiving_manager_name)
        target_employee = self._find_employee(target_employee_name)

        # Not promotable beyond VP
        if target_employee.role in ("Vice President", "President"):
            print(f"Error: {target_employee_name} cannot be promoted further.")
            return

        # Workers/Supervisors cannot be the receiving manager
        if receiving_manager.role in ("Worker", "Supervisor"):
            print(f"Error: {receiving_manager_name} cannot promote employees.")
            return

        # President cannot promote Workers (would be two levels)
        if receiving_manager.role == "President" and target_employee.role == "Worker":
            print("Error: Promotions can only be one level.")
            return
        
        

        # receiving manager must have a spot
        result = self._has_spots(receiving_manager)
        if result is False:
            print(f"Error: Receiving manager {receiving_manager_name} has reached maximum direct reports.")
            return

        # If there is a vacancy under receiving_manager that the target would not become boss of current peers
        for idx, report in enumerate(receiving_manager.reports):
            if isinstance(report, Vacancy) and (target_employee not in report.reports):
                # Move and promote
                if target_employee.role != "Worker":
                    self._replace_employee_with_vacancy(target_employee)
                else:
                    target_employee.boss.reports.remove(target_employee)
                target_employee.boss = receiving_manager
                target_employee.reports = receiving_manager.reports[idx].reports
                receiving_manager.reports[idx] = target_employee
                target_employee.promote()
                print(f"Successfully promoted {target_employee_name} under {receiving_manager_name}.")
                return

        # Otherwise, normal addition (no specific vacancy node needed)
        target_employee.boss.reports.remove(target_employee)
        target_employee.boss = receiving_manager
        receiving_manager.reports.append(target_employee)
        target_employee.promote()
        print(f"Successfully promoted {target_employee_name} under {receiving_manager_name}.")
        return

    def display_organization(self):
        # Displays the current organization hierarchy (Requirement 11).
        if self.president is None:
            print("Organization is empty.")
            return
        print(f"President: {self.president.name}")
        self._display_loop(self.president, 1)
        return

