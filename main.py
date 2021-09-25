# x = "   Hi this is s string "
# print(x.split()[1])
# print("the {2} {1} {0}".format("fox", "brown", "quick"))
# print("the {f} {b} {q}".format(f="fox", b="brown", q="quick"))
# result = 100/777
# print(f"The result was {:1.3f result}")


f = open("file.txt", "r")
lines = f.readlines()

student_arr = []

student = {}

for line in lines:
    if(line=='\n'):
        student_arr.append(student)
        student = {}
        continue

    info = line.strip().split()
    att = info[0][:-1]
    val = info[1]
    # print(att,val)
    if (att == "Regi"):
        val = int(val)
    elif(att == "CGPA"):
        val = float(val)
    student[att] = val

student_arr.append(student)
print(student_arr)
