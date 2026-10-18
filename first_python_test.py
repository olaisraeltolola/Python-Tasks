from unittest import TestCase

from contact_app_function import create_contact,clear_contacts

class TestPracticeFunction(TestCase):

	def test_that_new_contact_can_be_created_and_saved(self):

		clear_contacts()

		first_name = "Chizzy"
		last_name = "Ikokwu"
		phone_number = "09095321068"

		contact = create_contact(first_name, last_name, phone_number)

		self.assertEqual(type(contact), list)
		self.assertEqual(len(contact), 3)
		self.assertEqual("09095321068", contact[-1])


	def test_that_duplicate_contacts_cannot_be_created(self):

		clear_contacts()

		first_name = "Ekemini"
		last_name = "Udofa"
		phone_number = "09095321068"

		create_contact(first_name, last_name, phone_number)

		first_name = "Tolola"
		last_name = "Ola-Israel"
		phone_number = "09095321068"

		contact = create_contact(first_name, last_name, phone_number)

		self.assertIsNone(contact)

































































































































