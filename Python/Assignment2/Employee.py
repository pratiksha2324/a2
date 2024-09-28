from datetime import datetime

class AttendanceTracker:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee_name, attendance):
        """Adds an employee and their attendance record."""
        self.employees.append({
            "employee_name": employee_name,
            "attendance": attendance
        })

    def calculate_hours(self, clock_in, clock_out):
        """Calculates hours worked given clock-in and clock-out times."""
        time_format = '%H:%M'
        in_time = datetime.strptime(clock_in, time_format)
        out_time = datetime.strptime(clock_out, time_format)
        worked_hours = (out_time - in_time).seconds / 3600  # Convert seconds to hours
        return worked_hours

    def generate_report(self):
        """Generates a report of total hours worked and attendance patterns."""
        report = {}
        for employee in self.employees:
            total_hours = 0
            days_present = len(employee['attendance'])
            for date, times in employee['attendance'].items():
                if len(times) == 2:
                    hours = self.calculate_hours(times[0], times[1])
                    total_hours += hours
            report[employee['employee_name']] = {
                "total_hours": total_hours,
                "days_present": days_present
            }
        return report

    def attendance_summary(self):
        """Provides summary of employee attendance."""
        report = self.generate_report()
        if not report:
            print("No employee data available.")
            return

        highest_attendance = max(report.items(), key=lambda x: x[1]['days_present'])
        lowest_attendance = min(report.items(), key=lambda x: x[1]['days_present'])
        perfect_attendance = [employee['employee_name'] for employee in self.employees if len(employee['attendance']) == report[employee['employee_name']]['days_present']]
        most_absent = min(report.items(), key=lambda x: x[1]['days_present'])
        most_absent_list = [employee for employee, data in report.items() if data['days_present'] == most_absent[1]['days_present']]

        print("\nAttendance Summary:")
        print(f"Employee with the highest attendance: {highest_attendance[0]}, Days Present: {highest_attendance[1]['days_present']}")
        print(f"Employee with the lowest attendance: {lowest_attendance[0]}, Days Present: {lowest_attendance[1]['days_present']}")
        print(f"Employees with perfect attendance:")
        if perfect_attendance:
            for employee in perfect_attendance:
                print(employee)
        else:
            print("No employees with perfect attendance.")

        print("\nTotal Working Hours for Each Employee:")
        for employee, data in report.items():
            print(f"{employee}: {data['total_hours']} hours")

        print("\nEmployees with the most absences:")
        for employee in most_absent_list:
            print(employee)

# Example Usage
attendance_tracker = AttendanceTracker()
attendance_tracker.add_employee("Rajesh Deshpande", { "2024-08-15": ("09:00", "17:00"), "2024-08-16": ("09:15", "17:10"), "2024-08-17": ("09:30", "17:20")})
attendance_tracker.add_employee("Anjali Sharma", {"2024-08-15": ("08:45", "17:30"), "2024-08-16": ("09:00", "17:00")})
attendance_tracker.add_employee("Meena Kumari", {"2024-08-16": ("09:00", "18:00")})

attendance_tracker.attendance_summary()