import unittest

from mortgage_calculator.viewmodel.viewmodel import MortgageViewModel


class TestMortgageViewModel(unittest.TestCase):
    def setUp(self):
        self.view_model = MortgageViewModel()

    def test_by_default_button_calculate_monthly_payment_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_calculate_monthly_payment_state())

    def test_by_default_button_calculate_expected_term_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_calculate_expected_term_state())

    def test_by_default_button_calculate_overpaid_amount_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_calculate_overpaid_amount_state())

    def test_when_entered_correct_parameters_all_buttons_enabled(self):
        self.view_model.set_amount('1')
        self.view_model.set_initial_payment('1')
        self.view_model.set_rate('1')
        self.view_model.set_term('1')
        self.view_model.set_monthly_payment('1')

        self.assertNotEqual('disabled', self.view_model.get_button_calculate_monthly_payment_state())
        self.assertNotEqual('disabled', self.view_model.get_button_calculate_expected_term_state())
        self.assertNotEqual('disabled', self.view_model.get_button_calculate_overpaid_amount_state())

    def test_when_entered_incorrect_parameters_all_buttons_disabled(self):
        self.view_model.set_amount('1')
        self.view_model.set_initial_payment('')
        self.view_model.set_rate('1')

        self.assertEqual('disabled', self.view_model.get_button_calculate_monthly_payment_state())
        self.assertEqual('disabled', self.view_model.get_button_calculate_expected_term_state())
        self.assertEqual('disabled', self.view_model.get_button_calculate_overpaid_amount_state())

    def test_can_calculate_monthly_payment(self):
        self.view_model.set_amount('1')
        self.view_model.set_initial_payment('1')
        self.view_model.set_rate('1')
        self.view_model.set_term('1')
        self.view_model.set_monthly_payment('1')

        self.view_model.click_calculate_monthly_payment()

        self.assertEqual('0.0', self.view_model.get_click_calculate_monthly_payment_result())

    def test_can_calculate_expected_term(self):
        self.view_model.set_amount('1')
        self.view_model.set_initial_payment('1')
        self.view_model.set_rate('1')
        self.view_model.set_term('1')
        self.view_model.set_monthly_payment('1')

        self.view_model.click_calculate_expected_term()

        self.assertEqual('0', self.view_model.get_click_calculate_expected_term_result())

    def test_can_calculate_overpaid_amount(self):
        self.view_model.set_amount('1')
        self.view_model.set_initial_payment('1')
        self.view_model.set_rate('1')
        self.view_model.set_term('1')
        self.view_model.set_monthly_payment('1')

        self.view_model.click_calculate_overpaid_amount()

        self.assertEqual('0.0', self.view_model.get_click_calculate_overpaid_amount_result())

    def test_set_and_get_button_calculate_monthly_payment_state(self):
        value = 'enable'

        self.view_model.set_button_calculate_monthly_payment_state(value)
        result = self.view_model.get_button_calculate_monthly_payment_state()

        self.assertEqual(value, result)

    def test_set_and_get_button_calculate_expected_term_state(self):
        value = 'enable'

        self.view_model.set_button_calculate_expected_term_state(value)
        result = self.view_model.get_button_calculate_expected_term_state()

        self.assertEqual(value, result)

    def test_set_and_get_button_calculate_overpaid_amount_state(self):
        value = 'enable'

        self.view_model.set_button_calculate_overpaid_amount_state(value)
        result = self.view_model.get_button_calculate_overpaid_amount_state()

        self.assertEqual(value, result)

    def test_set_and_get_amount(self):
        value = '1'

        self.view_model.set_amount(value)
        result = self.view_model.get_amount()

        self.assertEqual(value, result)

    def test_set_and_get_initial_payment(self):
        value = '1'

        self.view_model.set_initial_payment(value)
        result = self.view_model.get_initial_payment()

        self.assertEqual(value, result)

    def test_set_and_get_rate(self):
        value = '1'

        self.view_model.set_rate(value)
        result = self.view_model.get_rate()

        self.assertEqual(value, result)

    def test_set_and_get_term(self):
        value = '1'

        self.view_model.set_term(value)
        result = self.view_model.get_term()

        self.assertEqual(value, result)

    def test_set_and_get_monthly_payment(self):
        value = '1'

        self.view_model.set_monthly_payment(value)
        result = self.view_model.get_monthly_payment()

        self.assertEqual(value, result)

    def test_set_and_get_term_type(self):
        value = 'months'

        self.view_model.set_term_type(value)
        result = self.view_model.get_term_type()

        self.assertEqual(value, result)

    def test_get_error_message(self):
        message = 'Errors: \n\tamount: \n\tinitial_payment: \n\trate: \n\tterm: \n\tmonthly_payment: \n'
        self.assertEqual(message, self.view_model.get_error_message())

    def test_errors_when_parse_string_with_incorrect_number(self):
        self.view_model.set_amount('1a')
        self.view_model.set_initial_payment('')
        self.view_model.set_rate('1akhbakdc')
        self.view_model.set_term('sdvsbdj')
        self.view_model.set_monthly_payment('sslnsnk')

        errors_not_empty = 'Incorrect values' in self.view_model.get_error_message()

        self.assertTrue(errors_not_empty)
