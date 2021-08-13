# inheritance in exception
# class MyError:
#     pass
# raise MyError()

# this will through TypeError: exceptions must derive from BaseException
# therefore it should inherint from BaseException like

class MyError(BaseException):
    pass

raise MyError()
