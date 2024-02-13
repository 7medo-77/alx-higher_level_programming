#!/usr/bin/python3
"""
Module that defines a square class that inherits form the Rectangle class
"""
from .base import Base
from .rectangle import Rectangle

class Square(Rectangle, Base):
	"""
	Squre class, which inherits from the rectangle class
	"""
	def __init__(self, size, x=0, y=0, id=None):
		"""
		Constructor for Square class with 3 private instance
		attributes
		"""
		super().__init__(size, size, x, y, id)

	@property
	def size(self):
		"""Getter Method for private attribute height"""
		return self.width


	@size.setter
	def size(self, width):
		"""Setter for virtual attribute size"""
		self.width = self.input_validator_dimension(width, "width")
		self.height = self.input_validator_dimension(width, "height")

	def __str__(self):
		"""String representation of the instance"""
		return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.width))

	def update(self, *args, **kwargs):
		"""
		Update methods that updates the attributes
		in the method paramters
		"""
		arg_dict = {1 :"id", 2 :"size", 3 :"x", 4 :"y"}
		if (args):
			for index, arg in enumerate(args):
				for key, value in arg_dict.items():
					if index + 1 == key:
						if (key == 2):
							arg = self.input_validator_axis(arg, value)
							self.size = arg
						elif (key == 3 or key == 4):
							arg = self.input_validator_axis(arg, value)
							setattr(self, value, arg)
						else:
							setattr(self, value, arg)
		else:
			for attribute, integer in kwargs.items():
				for key, value in arg_dict.items():
					if (value == attribute):
						if (key == 2):
							self.size = integer
						elif (key == 3 or key == 4):
							integer = self.input_validator_axis(integer, value)
							setattr(self, value, integer)
						else:
							setattr(self, value, integer)
