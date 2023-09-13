import hashlib


# 密码加密
def getPassword(password):
    if password is None or password == '':
        return ''
    else:
        md5 = hashlib.md5()
        md5.update(password.encode())
        result = md5.hexdigest()
        return result


if __name__ == '__main__':
    print(getPassword("root"))
