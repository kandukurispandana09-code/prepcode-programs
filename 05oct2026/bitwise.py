READ = int(input("enter a value"))
WRITE = int(input("enter a value"))
EXECUTE = int(input("enter a value"))
 
 user_permissions = READ| WRITE

 if user_permissions & READ:
    print("read premission is granted.")