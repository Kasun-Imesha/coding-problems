import torch


# x = torch.tensor(2., requires_grad=True)

# print(f"x: {x}")

# y = x**2 + 1

# y.backward()

# dx = x.grad

# print(f"grad: {dx}")


def find_grad(func, x):
    y = func(x)

    y.backward()

    return x.grad


def linear(x, m=1, c=0):
    return m*x + c


x = torch.tensor(2., requires_grad=True)
print(f"x: {x}")

print(find_grad(linear, x))