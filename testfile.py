   
class constat1_UserID:
    if __name__ == '__main__':
         f=open("/etc/passwd", "r")
         lines = f.readlines()
         list1_UserID = []
         with open("/etc/passwd", "r") as f:
           for line in lines:
             u_name = line.split(":")
             list1_UserID.append(u_name[0])
           print(list1_UserID)

