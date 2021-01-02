import re

class passport:

    def __init__(self):
        self.data = {}
        self.reqfields = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def isvalid(self):
        if not self.reqfields.issubset(set(self.data.keys())):
            return False
        if int(self.data["byr"]) < 1920 or int(self.data["byr"]) > 2002:
            return False
        if int(self.data["iyr"]) < 2010 or int(self.data["iyr"]) > 2020:
            return False
        if int(self.data["eyr"]) < 2020 or int(self.data["eyr"]) > 2030:
            return False
        hgtMatch = re.match( r'^(\d+)(in|cm)$', self.data["hgt"], re.M|re.I)
        if not hgtMatch:
            return False
        else:
            if hgtMatch.group(2) == "cm":
                if int(hgtMatch.group(1)) < 150 or int(hgtMatch.group(1)) > 193:
                    return False
            elif hgtMatch.group(2) == "in":
                if int(hgtMatch.group(1)) < 59 or int(hgtMatch.group(1)) > 76:
                    return False
        if not re.search( r'^#[0-9a-f]{6}$', self.data["hcl"], re.M|re.I):
            return False
        if not re.search( r'^(amb|blu|brn|gry|grn|hzl|oth)$', self.data["ecl"], re.M|re.I):
            return False
        if not re.search( r'^\d{9}$', self.data["pid"], re.M|re.I):
            return False

        return True

with open("4.input.txt", "r") as f:
    fcontent = f.read()

passports = []

for r in fcontent.split("\n\n"):
    p = passport()
    for field in r.split():
        parse = field.split(":")
        p[parse[0]] = parse[1]
    if p.isvalid():
        passports.append(p)

print(f"Valid passports: {len(passports)}")