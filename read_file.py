#Rread file and convert to list
def read_file(filename: str) -> list[int]:
    """
    Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
    """
    # Open the file
    # Read the file
    f=open(filename)
    s=[]
    l=f.read().split(',')
    for i in l:
        s.append(int(i))
    return s 

#Print list from file
print(read_file('data.txt'))
