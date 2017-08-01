import os
ldap_entry = """dn: EpsStaInfId=EpsStaInf,serv=EPS,mscId=aaaaaaa001aaaaaaa460040211064%s,ou=multiSCs,dc=o,dc=com
"""
IMSI = raw_input("IMSI NU: ")
ldap_entry = ldap_entry % IMSI

ldifFile = './460040211064%s.ldif' % IMSI
inFile = open(ldifFile, 'w')

count = 0

def getValue():
    EntryValue = raw_input("please the Value: ")
    return EntryValue

print "please choose modify type:\n1. add\n2. del\n3. modify\n4: End\n"

while True:
    Type = int(raw_input("TYPE: "))
    if Type == 4:
        print "ldif file context as following file: %s " % ldifFile
        inFile.writelines(ldap_entry)
        inFile.closed()
        break
    EntryName = raw_input("please input the entry Name: ")

    if count > 0:
        ldap_entry += '-\n'

    if Type == 1:
        ldap_entry += "add: %s\n" % EntryName
        ldap_entry += "%s: %s\n" % (EntryName, getValue())
    elif Type == 2:
        ldap_entry += "delete: %s\n" % EntryName
        ldap_entry += "%s: %s\n" % (EntryName, getValue())
    elif Type == 3:
        ldap_entry += "replace: %s\n" % EntryName
        ldap_entry += "%s: %s\n" % (EntryName, getValue())
    else:
        print "invalid value, please input again."
        continue

    count += 1
