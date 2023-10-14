class parent:
    def fun1(self):
        print("Iam Your parent")
class child1(parent):
    def fun2(self):
        print("Iam the child")
ob = child1()
# print(ob)
ob.fun1()