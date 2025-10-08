### 5. Trigonometry Example: Projectile Motion
import math

velocity = 20  # m/s
angle_deg = 45
angle_rad = math.radians(angle_deg)

# Range of projectile (no air resistance)
g = 9.81
range_ = (velocity ** 2) * math.sin(2 * angle_rad) / g

print(f"Projectile Range: {range_:.2f} meters")