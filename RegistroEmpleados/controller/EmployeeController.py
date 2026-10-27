import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from view.Terminal import Terminal
from model.Utilities.recOperator import RecOperator


class EmployeeController:
    def __init__(self):
        self.terminal = Terminal()
        self.rec_operator = RecOperator()

    def run(self):
        while True:
            self.terminal.clear_display()
            command = self.terminal.get_command()
            
            if command == 'exit':
                self.terminal.clear_display()
                self.terminal.display_message("Goodbye!")
                break
            elif command == 'create':
                self._create()
            elif command == 'read':
                self._read()
            elif command == 'update':
                self._update()
            elif command == 'delete':
                self._delete()
            
            self.terminal.wait_for_enter()

    def _create(self):
        self.terminal.clear_display()
        self.terminal.display_message("=== CREATE EMPLOYEE ===\n")
        
        try:
            emp_id = self.terminal.get_input("Enter ID: ")
            name = self.terminal.get_input("Enter Name: ")
            phone = self.terminal.get_input("Enter Phone: ")
            address = self.terminal.get_input("Enter Address: ")
            department = self.terminal.get_input("Enter Department: ")
            
            self.rec_operator.add(emp_id, name, phone, address, department)
            self.terminal.display_message("\nEmployee created successfully!")
        except ValueError as e:
            self.terminal.display_message(f"\nError: {e}")
        except Exception as e:
            self.terminal.display_message(f"\nError: {e}")

    def _read(self):
        self.terminal.clear_display()
        self.terminal.display_message("=== EMPLOYEES LIST ===\n")
        
        try:
            employees = self.rec_operator.read()
            
            if not employees:
                self.terminal.display_message("No employees found.")
                return
            
            print(f"{'ID':<10} {'Name':<25} {'Phone':<15} {'Address':<20}")
            print("-" * 70)
            
            for emp in employees:
                print(f"{emp['id']:<10} {emp['name']:<25} {emp['phone']:<15} {emp['address']:<20}")
                
        except Exception as e:
            self.terminal.display_message(f"Error: {e}")

    def _update(self):
        self.terminal.clear_display()
        self.terminal.display_message("=== UPDATE EMPLOYEE ===\n")
        
        try:
            emp_id = self.terminal.get_input("Enter ID to update: ")
            
            self.terminal.display_message("\nEnter new data (leave empty to keep current):")
            name = self.terminal.get_input("Enter Name: ")
            phone = self.terminal.get_input("Enter Phone: ")
            address = self.terminal.get_input("Enter Address: ")
            
            update_data = {}
            if name:
                update_data['name'] = name
            if phone:
                update_data['phone'] = phone
            if address:
                update_data['address'] = address
            
            if update_data:
                self.rec_operator.update(emp_id, **update_data)
                self.terminal.display_message("\nEmployee updated successfully!")
            else:
                self.terminal.display_message("\nNo changes made.")
        except KeyError:
            self.terminal.display_message("\nError: ID not found")
        except ValueError as e:
            self.terminal.display_message(f"\nError: {e}")
        except Exception as e:
            self.terminal.display_message(f"\nError: {e}")

    def _delete(self):
        self.terminal.clear_display()
        self.terminal.display_message("=== DELETE EMPLOYEE ===\n")
        
        try:
            emp_id = self.terminal.get_input("Enter ID to delete: ")
            
            self.rec_operator.delete(emp_id)
            self.terminal.display_message("\nEmployee deleted successfully!")
        except KeyError:
            self.terminal.display_message("\nError: ID not found")
        except Exception as e:
            self.terminal.display_message(f"\nError: {e}")
