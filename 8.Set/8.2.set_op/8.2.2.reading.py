n, m, k, x, y, z, t, a = map(int, [input() for _ in range(8)])

n_only = n - (n + m - x) - (n + k - z) + t
m_only = m - (n + m - x) - (m + k - y) + t
k_only = k - (n + k - z) - (m + k - y) + t

read_one = n_only + m_only + k_only
read_two = (n + m - x - t) + (m + k - y - t) + (n + k - z - t)
read_none = a - (n + m + k - (n + m - x) - (m + k - y) - (n + k - z) + t)

print(read_one)
print(read_two)
print(read_none)
