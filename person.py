# -*- coding: utf-8 -*-

class Person:
    def __init__(self, full_name, years, sex):
        """
        Constructor to initialize the Person object.

        Args:
        full_name (str): The individual's full name.
        years (int): The individual's age in years.
        sex (str): The individual's gender.
        """
        self.full_name = full_name
        self.years = years
        self.sex = sex

    def introduce_self(self):
        """
        Output an introduction for the person, including their name, age, and gender.
        """
        print("Hi, I’m {}. I’m {} years old and identify as {}.".format(self.full_name, self.years, self.sex))

    def is_adult(self):
        """
        Determine if the person is an adult (18 years or older).

        Returns:
        bool: True if the person is an adult, False otherwise.
        """
        return self.years >= 18


# Example Usage
if __name__ == "__main__":
    # Creating an instance of the Person class
    person_example = Person("Bob Smith", 22, "male")

    # Displaying the introduction
    person_example.introduce_self()

    # Check if the person is an adult
    if person_example.is_adult():
        print("{} is an adult.".format(person_example.full_name))
    else:
        print("{} is not an adult.".format(person_example.full_name))
