# Learning to Write

# Step 1: Create a list called snacks of at least 4 strings containing your favorite snacks.

# Step 2: Open a new file called shopping_list.txt in write mode as list_file.

# Step 3: Fill in this missing write() parameter in this loop to write your favorite snacks to the shopping list file.

for snack in snacks:
	list_file.write()
list_file.close()

# Step 4: Oh no! The loop above overwrites the file with each line, so we end up with only the last snack in the file. Let's fix this. Create a function called write_shopping_list() that takes 2 parameters: filename (the file to write to), and snacks (a list of strings). The function should use .writelines() to write your list of snacks to the filename.