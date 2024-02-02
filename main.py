# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import pandas as pd

# Load data from CSV file into a DataFrame
file_path = 'names.csv'
#  Read CSV file with no header
df = pd.read_csv('names.csv')

def countUniqueNames(billFirstName,billLastName,shipFirstName,shipLastName,billNameOnCard):
    # Edge case: None values are not allowed
    if (billFirstName == None or billLastName == None or  shipFirstName == None or  shipLastName == None or billNameOnCard == None):
        raise ValueError("None values are not allowed for input parameters.")
        return 0


    # Splitting names
    BFN = billFirstName.split()
    SFN = shipFirstName.split()
    BNOC = billNameOnCard.split()

    # Validate the number of name parts
    if (len(BFN) > 2  or len(BFN) < 1 or len(SFN) > 2  or len(SFN) < 1 or len(BNOC) > 3  or len(BNOC) < 2):
        raise ValueError("Invalid number of name parts in input parameters.")
        return 0

    # Initialize result variables
    BN = create(BFN,billLastName)
    SN = create(SFN,shipLastName)
    BC = create(BNOC[:-1],BNOC[-1])
    BCrev = [BC[2],BC[1],BC[0]]

    set1 = []
    add_to_set(set1,BN)
    add_to_set(set1,SN)
    add_to_set(set1,BC)
    set2 = []
    add_to_set(set2,BN)
    add_to_set(set2,SN)
    add_to_set(set2,BCrev)
    return min(len(set1),len(set2))

def are_strings_similar(str1, str2):
    if (str1 == -1 or str2==-1):
        return True
    if str1 == str2:
        return True  # Strings are the same
    if(are_names_nicknames(str1,str2)):
        return True


    len_diff = abs(len(str1) - len(str2))
    if len_diff > 1:
        return False  # More than one letter difference

    # Make sure str1 is the shorter string
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    i = 0
    j = 0
    diff_count = 0

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            diff_count += 1
            if len_diff == 0:
                i += 1  # Move shorter pointer if lengths are equal
        else:
            i += 1  # Move shorter pointer

        j += 1  # Always move longer pointer

    return diff_count <= 1

def are_names_nicknames(name1, name2):
    # Check if name1 is a nickname for name2
    is_name1_nickname2 = False
    is_name2_nickname1 = False
    r1 = df[df['name']==name1.lower()]


    # Check if name1 is a nickname for name2
    if not r1.empty:
        is_name1_nickname2 = (name2.lower() in r1.values[0])

    # Check if name2 is a nickname for name1
    r2 = df[df['name'] == name2.lower()]
    if not r2.empty:
        is_name2_nickname1 = (name1.lower() in r2.values[0])

    # Return True if either name1 is a nickname for name2 or name2 is a nickname for name1
    return (is_name1_nickname2 or is_name2_nickname1)


def eqaual(name1,name2):
     #Check if two names are equal, considering potential similarities in each part.
    # Check if each corresponding part of the names is similar
    if (are_strings_similar(name1[0],name2[0]) and are_strings_similar(name1[1],name2[1])
            and are_strings_similar(name1[2], name2[2])):
        return True
    return False


# Create a list containing parts of a name, considering a potential missing middle name.
def create(first_name, ln):
    res = first_name
    # Check if the first name has only one part (indicating a potential missing middle name)
    if len(first_name) == 1:
        res.append(-1)
    first_name.append(ln)
    return res

def has_mid(name):
    if name[1]==-1:
        return False
    return True

# Add a new name to a set of unique names, considering potential similarities.
def add_to_set(unique_names_set,new_name):
    for i in range (0,len(unique_names_set)) :
        # Check if the new name is similar to an existing unique name
        if(eqaual(unique_names_set[i],new_name)):
            # If the new name has a middle name and the existing one does not, update with the new name
            if (has_mid(new_name) and not has_mid(unique_names_set[i])):
                unique_names_set[i]= new_name
            return
    unique_names_set.append(new_name)