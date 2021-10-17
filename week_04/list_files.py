input_file = open("subjects.txt")
subjects = input_file.readlines()
subjects = [subject.strip() for subject in subjects]
[print(subject) for subject in subjects if subject[2] == '1']
input_file.close()