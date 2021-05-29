import unittest
import random_names


class Test(unittest.TestCase):

  def test_names(self):
    for i in range(500):
      FirstName = random_names.First()
      print(f"{FirstName=}")
      self.assertIsNotNone(FirstName)

      MiddleName = random_names.Middle()
      print(f"{MiddleName=}")
      self.assertIsNotNone(MiddleName)

      LastName = random_names.Last()
      print(f"{LastName=}")
      self.assertIsNotNone(LastName)

      FullName = random_names.Full()
      print(f"{FullName=}")
      self.assertIsNotNone(FullName)

      Company = random_names.Company()
      print(f"{Company=}")
      self.assertIsNotNone(Company)

      State = random_names.States()
      print(f"{State=}")
      self.assertIsNotNone(State)

      StateCode = random_names.StateCode()
      print(f"{StateCode=}")
      self.assertIsNotNone(StateCode)

      Address = random_names.Address()
      print(f"{Address=}")
      self.assertIsNotNone(Address)

      Place = random_names.Places() 
      print(f"{Place=}")
      self.assertIsNotNone(Place)

      Country = random_names.Country()
      print(f"{Country=}")
      self.assertIsNotNone(Country)


if __name__ == '__main__':
   unittest.main()
