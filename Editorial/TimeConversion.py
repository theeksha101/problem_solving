s = "12:09:55AM"
zn = s[-2:]
if zn == "PM" and s[:2] != "12":
    s = str(12 + int(s[:2])) + s[2:]
if zn == "AM" and s[:2] == "12":
    s = "00" + s[2:]
print(s[:-2])