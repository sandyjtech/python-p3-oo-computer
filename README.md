# OO Computer Lab

## Learning Goals

- Gain proficiency instantiating a class
- Gain ability when to configure attributes as `properties` with `getter` and `setter` methods
- Practice protecting 'private' properties by omitting setters after initialization

## Introduction

To practice object oriented programming (OOP), you're going to create a `Computer` class. Each instance of the class will have the ability to:

- report its specs
- store a file
- delete a file
- upgrade memory

## A Note on Notation

In the instructions below, you'll see the class constructor, instance methods, and properties referenced with different notation.
- `Class_Name(optional_values)` indicates invoking a class's constructor to create a new instance of the class
- `Class attribute` indicates that instances of this class should possess this attribute (no getter or setter method needed)
- `Class property attribute` indicates that an attribute should be configured as a property for instances of the class, with getter and setter methods assigned as needed
- `Class method_name(self, *optional_args)` indicates an instance method of the class
- `Class class attribute` indicates that this attribute should be added to the class scope
- `Class classmethod method(cls)` indicates this method should be added to the class scope 

## Instructions

Create a `Computer` class with the follwing attributes and behavior:

- `Computer(brand, model)`: takes string arguments of a brand an model and assigns them as attributes to the created instance. The computer's model and brand _should not_ be able to change after initialization. When a new computer is created, it should have the following attributes in addition to its brand and model (assigned to instance variables):
    - `memory_GB` with an initial value of 8
    - `storage_free` with an initial value of 1000
- `Computer property brand` should get (but not set) the computer's brand
- `Computer property model` should get (but not set) the computer's model
- `Computer property memory_GB` should get and set the value of the memory as appropriate
- `Computer property storage_free` should get and set the value of the computer's free storage. The maximum value allowed is 1000 and the minimum value allowed is 0.

### Additional methods

- `Computer upgrade_memory(self, RAM)`: takes a dictionary (`{model: str, size: int}`) and adds the size of the RAM to the computer's memory
- `Computer is_disk_full(self, file_size)`: receives a file_size number and returns `True` if the free storage space is less than the file size: otherwise returns `False`
- `Computer save_file(self, file)`: given a file dictionary (`{name: str, size: int}`), this method will first use a helper method to check whether the disk has enough space to save the file. If there _is_ enough space, reduce the value of `storage_free` by the file size, and return the string `"f{file['name']} has been saved!"`, but if there is not enough space, return the string `f"There is not enough space on disk to save {file['name']}."`
- `Computer delete_file(self, file)`: given a file dictionary (`{name: str, size: int}`), make the appropriate adjustment to the free storage size and return a string confirming that the file has been deleted which includes the file's name.
- `Computer specs(self)`: returns a string which includes both the current memory and free storage, both in gigabytes.
- `Computer classmethod brands(cls)`: returns a list of unique strings of all of the computer brands that have been instantiated (no duplicates).
- `Computer classmethod models(cls)`: returns a list of unique strings of all of the computer models that have been instantiated (no duplicates).
- `Computer classmethod largest_memory(cls)`: returns the instance of the computer with the largest memory.