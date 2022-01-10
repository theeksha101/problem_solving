class UserMainCode(object):
    def total_turns(self, string, m, n):
        harry_string = string[-m]
        new_string = harry_string + string[:-m]
        count = 1
        while new_string != string:

    def harry_string(self, string):
        


user_main_code = UserMainCode()
print(user_main_code.total_turns("AbcDef", 1, 2))
