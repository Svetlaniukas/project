import unittest
import json
import os
import sys
sys.path.insert(0, '/Users/svetlanamelichova/Desktop/wooden-products-website')
from app import app
from app.utils import save_order  # Импорт функции save_order из файла utils.py
from flask_testing import TestCase


class FlaskTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    # Тест главной страницы на доступность
    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Тест отправки данных через форму на главной странице
    def test_index_post(self):
        response = self.client.post('/', data=dict(
            name="Test Name",
            phone="123456789",
            email="test@example.com",
            inquiryType="General",
            county="Test County",
            message="Test Message"
        ))
        self.assertEqual(response.status_code, 200)
        # Добавьте дополнительные проверки содержимого ответа здесь

    # Тест маршрута /send_email
    def test_send_email(self):
        response = self.client.post('/send_email', data=dict(
            name="Test Name",
            phone="123456789",
            email="test@example.com",
            inquiryType="General",
            county="Test County",
            message="Test Message"
        ))
        self.assertEqual(response.status_code, 200)
        # Проверьте JSON ответа здесь, например:
        data = json.loads(response.data)
        self.assertEqual(data["message"], "Email Sent and Data Saved!")

    # Тест функции save_order
    def test_save_order(self):
        order_data = {"test": "data"}
        result = save_order(order_data)
        self.assertTrue(result)

        with open('orders.json', 'r') as file:
            orders = json.load(file)
        self.assertIn(order_data, orders)

    # Очистка после теста
    @classmethod
    def tearDownClass(cls):
        if os.path.exists('orders.json'):
            os.remove('orders.json')


if __name__ == '__main__':
    unittest.main()
