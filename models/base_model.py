#!/usr/bin/python3
"""[summary]
"""


import uuid
from cmd import Cmd
import datetime


class BaseModel():
	"""[summary]
	"""

	def __init__(self, *args, **kwargs):
		"""[summary]
		"""
		if kwargs is not None and len(kwargs) != 0:
			for key, value in kwargs.items():
				if key == "__class__":
					pass
				elif key == "created_at":
					self.created_at = datetime.datetime.strptime((kwargs["created_at"]), "%Y-%m-%dT%H:%M:%S.%f")
				elif key == "updated_at":
					self.updated_at = datetime.datetime.strptime((kwargs["updated_at"]), "%Y-%m-%dT%H:%M:%S.%f")
				else:
					setattr(self, key, value)

		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.datetime.today()
			self.updated_at = datetime.datetime.today()
      
	def __str__(self):
		"""[summary]
		"""
		return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
	
	def save(self):
		"""[summary]
		"""
		self.updated_at = datetime.datetime.today()
	
	def to_dict(self):
		"""[summary]
		"""
		my_dict = self.__dict__.copy()
		my_dict["__class__"] = "BaseModel"		
		my_dict["updated_at"] = self.updated_at.isoformat()
		my_dict["created_at"] = self.created_at.isoformat()
		#new_dict[__class__] = BaseModel
		#new_dict[updated_at] = str(self.updated_at)
		#new_dict[created_at] = str(self.created_at)
		return my_dict

