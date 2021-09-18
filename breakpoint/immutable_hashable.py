# all immutable objects are hashable but not all hashable are immutable
# string, tuple , integer, boolean are immutabel and hashable
# we can't put unhashable object inside set
# s = {'hello', [1, 2, 3], 2, (1, 2, 3), True} # throws an error list [1, 2, 3] is unhashble

