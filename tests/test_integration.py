

import pytest
from app import app

class TestAPI:
    """Tests de integración para la API Flask"""
    
    def setup_method(self):
        """Configura el cliente de pruebas"""
        self.client = app.test_client()
        app.config['TESTING'] = True
    
    def test_home(self):
        """Prueba el endpoint principal"""
        response = self.client.get('/')
        assert response.status_code == 200
        data = response.get_json()
        assert 'message' in data
        assert 'endpoints' in data
    
    def test_add_endpoint(self):
        """Prueba el endpoint de suma"""
        response = self.client.get('/add?a=5&b=3')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 8
    
    def test_subtract_endpoint(self):
        """Prueba el endpoint de resta"""
        response = self.client.get('/subtract?a=10&b=4')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 6
    
    def test_multiply_endpoint(self):
        """Prueba el endpoint de multiplicación"""
        response = self.client.get('/multiply?a=3&b=7')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 21
    
    def test_divide_endpoint(self):
        """Prueba el endpoint de división"""
        response = self.client.get('/divide?a=20&b=5')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 4
    
    def test_divide_by_zero_endpoint(self):
        """Prueba el manejo de error al dividir por cero"""
        response = self.client.get('/divide?a=10&b=0')
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
