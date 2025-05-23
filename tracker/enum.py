from enum import Enum

class Category(Enum):
    FOOD = "food"
    DRINKS = "drinks"
    BILLS = "bills"
    UTILITIES = "utilities"
    INVESTMENT = "investment"
    TRANSPORTATION = "transportation"
    SHOPPING = "shopping"
    MEDICAL = "medical"
    EDUCATION = "education" 
    TAXES = "taxes" 
    INSURANCE = "insurance"
    SALARY = "salary"
    
class Cashflow_Type(Enum):
    INCOME = "income" 
    EXPENSE = "expense"