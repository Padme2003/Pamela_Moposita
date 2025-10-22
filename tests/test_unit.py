

import pytest
from calculator import Calculator

class TestCalculator:
    """Tests unitarios para la clase Calculator"""
    
    def setup_method(self):
        """Se ejecuta antes de cada test"""
        self.calc = Calculator()
    
    def test_add(self):
        """Prueba la suma de dos números"""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
    
    def test_subtract(self):
        """Prueba la resta de dos números"""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
    
    def test_multiply(self):
        """Prueba la multiplicación de dos números"""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(0, 5) == 0
    
    def test_divide(self):
        """Prueba la división de dos números"""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(9, 3) == 3
    
    def test_divide_by_zero(self):
        """Prueba que se lance error al dividir por cero"""
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)