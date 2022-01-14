def sort():
    BB = [14,33,27,35,10]
    CC = []
    #print(BB)
    #print(CC)
    for i in range(len(BB)-1):
         for a in range(len(BB)-1):
             if BB[a] < BB[a+1]: #สลับ
                # +BB[x] ก่อน
                if CC.count(BB[a]) == 1:
                    CC.remove(BB[a]) # -ออก
                    CC.append(BB[a]) # +เข้า
                    print(1)
                    print(CC)
                else:
                    CC.append(BB[a]) # +เข้า
                    print(2)
                    print(CC)
                # +BB[x-1] ทีหลัง (>กว่า)
                if CC.count(BB[a+1]) == 1:
                    CC.remove(BB[a+1]) # -ออก
                    CC.append(BB[a+1]) # +เข้า
                    print(3)
                    print(CC)
                else:
                    CC.append(BB[a+1]) # +เข้า
                    print(4)
                    print(CC)

sort()
