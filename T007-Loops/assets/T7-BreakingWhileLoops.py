# Breaking While Loops

# Step 1: Run the following while loop and see what happens!

counter = 0

while counter < 100:
  print(f"Counter: {counter}")
  counter += 1

  # If counter is 25, loop breaks
  if counter == 25:
    break

 # Step 2: Try changing the break keyword to continue. What happens now?

 # Step 3: Try changing the order of the lines in the loop. What happens if you place the print statement after the conditional? The counter increment? Play around with the different ways you can break loops in Python!