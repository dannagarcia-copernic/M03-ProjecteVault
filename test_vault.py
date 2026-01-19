import unittest
from vault_security import check_password

class TestVaultSecurity(unittest.TestCase):
    def test_password_length(self):
        self.assertFalse(check_password("Ab1")) # Curta

    def test_password_no_numbers(self):
        self.assertFalse(check_password("PasswordSinNumeros"))

    def test_password_no_upper(self):
        self.assertFalse(check_password("passwordcon123"))

    def test_password_admin(self):
        self.assertFalse(check_password("Admin12345")) # Conté admin

    def test_password_correct(self):
        self.assertTrue(check_password("Segura_2026")) # Aquesta hauria de passar

if __name__ == '__main__':
    unittest.main()
