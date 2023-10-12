import platform

print(platform.system())
if platform.system()=='Linux':
    print("It is linux")
else:
    print('It is not linux')