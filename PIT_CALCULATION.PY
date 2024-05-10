class Employee:
    def __init__(self, name: str, salary: float, position: str, organization_type: str, education: str, children: int = 0):
        
        self.name = name
        self.salary = salary
        self.position = position
        self.organization_type = organization_type
        self.education = education
        self.children = children

    def calculate_tax(self) -> float:   #tax is calculated based on employees income  
        gross_income = self.salary     
        deductions = self.calculate_deductions()   
        taxable_income = gross_income - deductions       
        tax = self.calculate_tax_rate(taxable_income)  # Calculate tax based on taxable income
        return tax

    def calculate_deductions(self) -> float:
        deductions = 0
        if self.position == "Regular" and self.organization_type!= "Government":   
            deductions = self.salary * 0.10
        elif self.position == "Contract" and self.organization_type!= "Government":
            deductions = self.salary * 0  # pf deduction
        elif self.organization_type =='private':
            deductions += self.salary * 0.05  # pf deduction
        deductions += self.salary * 0.2      #GIS deduction
        if self.education:
            deductions += 350000      # Education allowance deduction
        deductions += self.children * 350000   # Children education expense deduction
        return deductions

    def calculate_tax_rate(self, tax: float) -> float:
        if tax <= 300000:
            tax += tax * 0
        elif 300001 <= tax <= 400000:
            tax += tax * .1
        elif 400001 <= tax <=  650000:
            tax += tax * .15
        elif  650001 <= tax <= 1000000:
            tax += tax * .20
        elif 100001 <= tax <= 1500000:
            tax += tax * .25
        elif tax <= 1500001:
            tax += tax * .30 
        return tax


class TaxCalculator:
    def __init__(self, employee: Employee):
        self.employee = employee

    def calculate_tax(self) -> float:
        return self.employee.calculate_tax()


name = input('enter employee name: ')
salary = float(input("Enter salary income: "))
position = input("Are you a contract employee? (yes/no): ").lower() == 'yes'
organization_type = input('private or public:').lower()
education = int(input('how many children are going to school: '))

employee = Employee(name, salary, "Regular" if not position else "Contract", organization_type, str(education))
tax_calculator = TaxCalculator(employee)
print("Tax:", tax_calculator.calculate_tax())