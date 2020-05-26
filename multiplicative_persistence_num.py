class Persistence():

    def my_list(self, num):
        mylist = []
        while num:
            num, listnum = divmod(num, 10)
            mylist.append(listnum)
        return mylist

    def mul_all(self,mylist):
        multiplier = 1
        while mylist:
            multiplier *= mylist.pop()
        return multiplier

    def multiplicative_persistence(self):
        num = int(input('enter num: '))
        count = 0
        while num >= 10:
            num = self.mul_all(self.my_list(num))
            count += 1
        return 'result: ' + str(count)

print(Persistence().multiplicative_persistence())


