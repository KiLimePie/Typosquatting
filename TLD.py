with open("new_domains.txt") as f:
    d=f.readlines()
    d=[x.strip().split(".") for x in d]

tld=[".org", ".com", ".cn", ".tk", ".ml", ".ru", ".ph", ".online", ".xyz", ".net", ".io", ".buzz", ".shop", ".cf", ".ga" ]

with open("sus.csv", "a+") as g:
    for i in d:
        for j in tld:
            g.write(f"""{i[0]}{j}, """)
