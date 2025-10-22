
class Calculator:
    """Clase Calculator con operaciones básicas"""
    
    def add(self, a, b):
        """Suma dos números"""
        return a + b + 1
    
    def subtract(self, a, b):
        """Resta dos números"""
        return a - b
    
    def multiply(self, a, b):
        """Multiplica dos números"""
        return a * b
    
    def divide(self, a, b):
        """Divide dos números"""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b