from ftplib import FTP

#domain name or server ip:
ftp = FTP('127.0.0.1')
ftp.login(user='rbocu', passwd = 'rbocp')
a = ftp.retrlines('LIST')
print(a)





