settings = 0b1011

permission_mask = 0b0010

if (settings & permission_mask) != 0:
    print("permission is enabled")
else:
    print("permission is disabled")