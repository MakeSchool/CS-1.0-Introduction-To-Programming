# Step 1: Here are the empty functions for our version of the Python poet - write tests for each function by printing out what the returned value would be for 2 different inputs. You can follow the example shown for the first function!

# # Project: Python Poet
from random import randint

def get_file_lines(filename):
  """
  Read in a poem and converts the text to a list of lines
  Parameters: filename - path of poetry .txt file
  Returns: lines_list - list of lines from the poem text
  """
  pass # This tells python the function isn't filled in yet, but will be soon!

def lines_printed_backwards(lines_list):
  """ 
  Print a poem backwards with original line numbers
  Parameters: lines_list - List of poem lines
  Returns: None
  """
  pass

def lines_printed_random(lines_list):
  """ 
  Print random lines from the poem to create a random poem of the same length
  Parameters: lines_list - List of poem lines
  Returns: None
  """
  pass

def lines_printed_custom(lines_list):
  """ 
  Print all even lines followed by all odd lines
  Parameters: lines_list - List of poem lines
  Returns: None
  """
  pass


# Test our functions!
print(get_file_lines('remember_joy_harjo.txt'))
print(get_file_lines('this_file_doesnt_exist.txt'))