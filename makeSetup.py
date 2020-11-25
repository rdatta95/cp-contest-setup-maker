supported_sites = {
    "codeforces" : ("www.codeforces.com"),
    "codechef"   : ("www.codechef.com")
}

site_number = 1
print("Choose site:")
for site in supported_sites.keys():
    print("{0}. {1}".format(site_number, site))
    site_number += 1
selection = int(input("Enter Choice : ").strip())
site = list(supported_sites.keys())[ selection - 1 ]

contest = input("Enter Contest Code : ")

print( supported_sites[ site ] + "/" + contest)
