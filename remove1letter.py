l = []

domain=input("Enter the domain name you would like to modify: ")
tld=input("Enter the top level domain (.com, .org, etc): ")

for i,ch in enumerate(domain):
    l.append(domain[:i] + domain[i+1:])

for i in l:
  print((i)+(tld))