#Create a program that reads a file and writes a modified version to a new file.
with open("input.txt","r") as file, open("output.txt","w") as outfile:
    for line in file:
        modified_line = line.upper()
        outfile.write(modified_line)

#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
while True:
  filename = input("Enter the file name: ")
  try:
    with open(filename, "r") as file:
      print(file.read())
      break #break is only used in a loop, to stop the loop once a valid file has been entered.
  except FileNotFoundError:
    print("File not found. Please try again.")
  finally:
    print("Thank you for using this service.") #once the execution ends, the user gets the thank you message
