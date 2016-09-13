import os
import sys


GOPRO_MAIN_FILE_PREFIX = 'GOPR'
GOPRO_SHORTENED_FILE_PREFIX = 'GP'

########### Fill in this personal information #########
# First/Last Name
OWNER = "First/Last Name" 
# Contact Phone number
PHONE_NUMBER = "555-555-5555"
# Contact email address
EMAIL = "Email@emaildomain.com"
#######################################################


def main(args):
    if len(args) < 2:
        print('Error, missing argument for folder')
        sys.exit(1)
    folder_location = args[1]
    if folder_location[-1] == '/':
        folder_location = folder_location[0:len(folder_location)-1]

    files = os.listdir(folder_location)
    file_groupings = dict()
    for file in files:
        if os.path.isdir(file):
            continue
        numbers = file[len(GOPRO_MAIN_FILE_PREFIX):file.rfind('.')]
        if file.startswith(GOPRO_MAIN_FILE_PREFIX):
            numbers_list = list()
            numbers_list.append(file)
            file_groupings[numbers] = numbers_list
        elif file.startswith(GOPRO_SHORTENED_FILE_PREFIX):
            file_groupings[numbers].append(file)

    for k, v in file_groupings.items():
        if len(v) < 2:
            continue
        new_folder = folder_location + '/' + GOPRO_MAIN_FILE_PREFIX + str(k)
        if not os.path.isdir(new_folder):
            os.mkdir(new_folder)
        for val in v:
            new_file_path = new_folder + '/' + val
            old_file_path = folder_location + '/' + val
            os.rename(old_file_path, new_file_path)

def writeContactInfo(args):
    if OWNER == "First/Last Name" or PHONE_NUMBER == "555-555-5555":
        print('Error: Personal information not set')
        sys.exit(1)
    file = open(args[1]+"\Owner_Contact.txt", "w")
    file.write("Owner: " + OWNER + "\n")
    file.write("Number: " + PHONE_NUMBER+ "\n")
    file.write("EMAIL: " + EMAIL+ "\n")
    file.close()

if __name__ == '__main__':
    main(sys.argv)
    writeContactInfo(sys.argv)
