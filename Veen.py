import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots()


circle1 = Circle((0.3, 0.5), 0.2, color='blue', alpha=0.5, label="Diet Soda")
circle2 = Circle((0.5, 0.5), 0.2, color='green', alpha=0.5, label="Brussels Sprouts")


ax.add_patch(circle1)
ax.add_patch(circle2)

plt.text(0.2, 0.5, '28%', ha='center', va='center', fontsize=10)  
plt.text(0.5, 0.5, '19%', ha='center', va='center', fontsize=10)  
plt.text(0.4, 0.5, '36%', ha='center', va='center', fontsize=10)  
plt.text(0.75, 0.5, '17%', ha='center', va='center', fontsize=10)  


ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', 'box')
plt.title("Diet Soda and Brussels Sprouts Preferences")


ax.axis('off')
plt.legend(loc='upper right')
plt.show()
