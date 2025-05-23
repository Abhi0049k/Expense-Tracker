from datetime import datetime
from .enum import Cashflow_Type, Category

class Transaction:
    def __init__(self, id, amt, title, cashflow_t, category, date=None, time=None):
        now = datetime.now()
        self.__id = id
        self.__amount = amt;
        self.__title = title;
        self.__date = date if date is not None else now.date();
        self.__time = time if time is not None else now.time();
        self.__cashflow_type = cashflow_t;
        self.__category = category;
        
    def __repr__(self):
        return f"{self.__title}: {self.__amount} | {self.__cashflow_type} | {self.__category} | {self.__date} {self.__time}"
    
    @property
    def id(self):
        return self.__id
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, new_title):
        if not new_title:
            raise ValueError("Title cannot be empty!")
        self.__title = new_title
        print("Title updated Successfully!")
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amt):
        if not amt:
            raise ValueError("Amount cannot be empty!")
        self.__amount = amt  
    
    @property
    def cashflow_type(self):
        return self.__cashflow_type
    
    @cashflow_type.setter
    def cashflow_type(self, cft):
        if not isinstance(cft, Cashflow_Type):
            raise ValueError("Cashflow type must be an instance of cashflow type enum!")
        self.__cashflow_type = cft.value
    
    @property 
    def category(self):
        return self.__category
    
    @category.setter 
    def category(self, cgt):
        if not isinstance(cgt, Category):
            raise ValueError("Category must be an instance of Category type enum!")
        self.__category = cgt.value
    
    @property
    def date(self):
        return self.__date
    
    @property
    def time(self):
        return self.__time