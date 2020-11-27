import codeforces

supported_sites = ["codeforces", "codechef"]

for index in range(0, len(supported_sites)):
    print("{0}. {1}".format(index + 1, supported_sites[index]))
choice = int(input("Select site : ").strip())

site = supported_sites[choice - 1]
if site == "codeforces":
    codeforces.makeSetup()
else:
    pass 