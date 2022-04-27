import gorilla_lib


def monkey_f(self):
    print("monkey_f() is being called")


gorilla_lib.DEMO_VAR = 'sorry, it"s just a programming'

# replacing address of "func" with "monkey_f"
gorilla_lib.A.func = monkey_f
obj_gor = gorilla_lib.A()
# calling function "func" whose address got replaced
# with function "monkey_f()"
obj_gor.func()  # monkey_f() is being called


print(gorilla_lib.DEMO_VAR)
