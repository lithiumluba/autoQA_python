# To Do: Write decorator skip_if that takes two arguments:
# - condition: boolean expression
# - reason: string, default value empty string
# If condition is calculated as True,
# function shouldn't be performed and if reason is not empty, reason should be printed
# If condition is False, then function should be performed as usual

def skip_if(condition, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                if reason:
                    print(reason)
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator

print('Test_1')
@skip_if(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
  assert 2 + 2 == 5

test_two_plus_two()  # 'Skipped because of JIRA-123 bug' is printed

print('Test_2')
@skip_if(condition=False, reason='Skipped because of JIRA-123 bug')
def test_two_minus_two():
   assert 2 - 2 == 5

# test_two_minus_two()  # assertion error
try:
    test_two_minus_two()  # This should raise an AssertionError
except AssertionError:
    print("AssertionError occurred as expected")
