#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT
# Author: Hiroshi Harada
# Date: March 15, 2026

import numpy as np
import matplotlib.pyplot as plt

def collatz_path(n):
    path = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        path.append(n)
    return path

# Function to calculate the root (source) of a 4m+1 magazine
def get_magazine_root(n):
    while n % 4 == 1 and n > 1:
        n = (n - 1) // 4
    return n

# Function to generate a sequence of 4m+1 reductions
def generate_4m_plus_1_seq(start, length=8):
    seq = [start]
    for _ in range(length - 1):
        seq.append(seq[-1] * 4 + 1)
    return np.array(seq)

# Auto-tracking radar function for the Log2 Collatz Spiral
def generate_radar_spiral(n_val):
    path_n = collatz_path(n_val)
    path_n_r = np.log2(path_n)
    path_n_theta = path_n_r * 2 * np.pi

    # Extract all odd numbers the trajectory passes through (radar detection)
    odd_numbers = sorted(list(set([num for num in path_n if num % 2 != 0])))

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(12, 12))
    fig.patch.set_facecolor('#0d0d0d')
    ax.set_facecolor('#0d0d0d')

    # Plot 2^b main line (Real axis / Final convergence)
    max_r = int(np.max(path_n_r)) + 3
    powers_of_2 = np.array([2**i for i in range(1, max_r + 1)])
    r_2b = np.log2(powers_of_2)
    ax.plot(r_2b * 2 * np.pi, r_2b, color='red', alpha=0.7, linewidth=1, linestyle=':', zorder=4)
    ax.scatter(r_2b * 2 * np.pi, r_2b, color='red', alpha=0.7, s=20, zorder=5, label='2^b Main Line')

    # Dynamic generation: Glide launchers (a * 2^b)
    first_gold = True
    for a in odd_numbers:
        if a == 1:
            continue
        max_power = max_r + 3
        powers_of_2_times_a = np.array([a * 2**i for i in range(max_power)])
        r_a = np.log2(powers_of_2_times_a)
        theta_a = r_a * 2 * np.pi
        label_gold = 'a*2^b Glide Launcher' if first_gold else ""
        ax.plot(theta_a, r_a, color='gold', alpha=0.7, linewidth=1, linestyle=':', zorder=4, label=label_gold)
        ax.scatter(theta_a, r_a, color='gold', alpha=0.7, s=20, zorder=5)
        first_gold = False

    # Dynamic generation: Roots of 4m+1 cooling magazines
    magazine_roots = sorted(list(set([get_magazine_root(a) for a in odd_numbers])))
    for i, root in enumerate(magazine_roots):
        seq = generate_4m_plus_1_seq(root, length=8)
        r = np.log2(seq)
        theta = r * 2 * np.pi
        label_lime = '4m+1 Magazine' if i == 0 else ""
        ax.plot(theta, r, color='lime', alpha=0.7, linewidth=1, linestyle='--', zorder=4, label=label_lime)
        ax.scatter(theta, r, color='lime', alpha=0.7, s=20, zorder=5)

    # Plot the trajectory of n on the top layer
    ax.plot(path_n_theta, path_n_r, color='cyan', linewidth=2, label=f'Trajectory of n={n_val}', zorder=10)
    ax.scatter(path_n_theta, path_n_r, color='cyan', s=50, zorder=11)

    ax.set_rticks([])
    ax.set_yticklabels([])
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.grid(True, color='gray', alpha=0.3)

    handles, labels = ax.get_legend_handles_labels()
    unique_labels = dict(zip(labels, handles))
    ax.legend(unique_labels.values(), unique_labels.keys(),
              loc='upper right', bbox_to_anchor=(1.3, 1.1),
              fontsize=10, facecolor='#1a1a1a', labelcolor='white')

    plt.title(f"Log2 Collatz Spiral: Auto-Tracking Radar (n={n_val})",
              pad=20, fontsize=16, fontweight='bold', color='white')
    plt.tight_layout()

    filename = f'collatz_log2_radar_{n_val}.png'
    plt.savefig(filename)
    print(f"Saved: {filename}")
    plt.show()
    plt.close()

# ---- Natural number list Input (1–1000 OK) ----
numbers_to_test = [5,7]  

for n_val in numbers_to_test:
    generate_radar_spiral(n_val)


# In[ ]:




