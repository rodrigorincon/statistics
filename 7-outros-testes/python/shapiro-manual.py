import numpy as np
from scipy import stats

original_sample = [1.906, 2.103, 1.522, 2.618, 1.427, 2.225, 1.697, 3.154, 1.985, 1.996, 1.71]
average = np.mean(original_sample)
size_x = len(original_sample)

x = np.sort(original_sample) # sort sample

ss = sum([ (i-average)**2 for i in x])

# as python libs doesnt get the A coeficients and the calculation is a bit hard, we will hardcoded them for this example
a_list = [0.5601, 0.3315, 0.2260, 0.1429, 0.0695]

# for-loop to calculate the B value
limit_loop = int(size_x/2) if size_x%2 == 0 else int((size_x+1)/2)
b = 0
for i in range(limit_loop):
  amplitude = x[size_x-i-1] - x[i]
  a = a_list[i] if i < len(a_list) else 0
  b += a*amplitude
  print(f'Loop {i}: A {a:.4f} Amplitude {amplitude:.4f} = B {(a*amplitude):.4f}')

w = b**2 / ss

print(f'SS: {ss:.4f}')
print(f'B: {b:.4f}')
print(f'W: {w:.4f}')

# as we don't have this W value in the table, we need to interpolate the closest values.
y0 = 0.876
y1 = 0.940
x0 = 0.1
x1 = 0.5
p_value = (w - y0) * (x1 - x0) / (y1 - y0) + x0
print(f'P-value: {p_value:.4f}')

if p_value < 0.05:
  print('Sample is not normal')
else:
  print('Sample is normal')

### Running shapiro lib function
w, p_value = stats.shapiro(original_sample)
print(f'\nBy Scipy function: W={w:.4f}, p-value={p_value:.4f} \n')

### Check the Shapiro function to a real normal curve
normal_data = np.random.normal(loc=0, scale=1, size=100)
w, p_value = stats.shapiro(normal_data)
print(f'Values for a real normal data. W={w:.4f}, p-value={p_value:.4f}')

# The p-value decrease with less data, but the W still high
normal_data = np.random.normal(loc=0, scale=1, size=10)
w, p_value = stats.shapiro(normal_data)
print(f'Values for a real normal data. W={w:.4f}, p-value={p_value:.4f}')