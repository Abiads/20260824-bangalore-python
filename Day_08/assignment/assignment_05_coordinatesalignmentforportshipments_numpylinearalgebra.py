"""
### Assignment 5: Coordinates Alignment for Port Shipments (NumPy Linear Algebra)
#### Scenario
A shipping port logs the $(x, y)$ coordinate offsets of customer cities relative to a central hub. To calibrate satellite distances, the coordinates must be translated relative to a new port dock and rotated to align with the camera angle.

#### Problem Description
Write a function `align_customer_coordinates(coordinates, angle_degrees, dock_offset)`:
1. `coordinates` is a 2D NumPy array of shape `(N, 2)` representing $(x, y)$ coordinate offsets.
2. `angle_degrees` is the rotation angle in degrees (float). Convert this angle to radians:
   $$\theta = \text{angle\_degrees} \times \frac{\pi}{180}$$
3. Construct the 2D **Rotation Matrix** $R$:
   $$R = \begin{pmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{pmatrix}$$
4. **Determinant Verification**: Calculate the determinant of the rotation matrix $R$ using `np.linalg.det(R)`.
   - If the absolute difference between the determinant and `1.0` is greater than `1e-6` (i.e. $|\text{det} - 1.0| > 10^{-6}$), raise a `ValueError` with the message `"Invalid rotation matrix."`
5. **Transformation Sequence**:
   - **Translation**: Translate the points by adding `dock_offset` (a 1D array of shape `(2,)` representing $[dx, dy]$) to `coordinates` using broadcasting.
   - **Rotation**: Rotate the translated points by multiplying them by the rotation matrix.
     $$\text{Aligned Coordinates} = \text{Translated Coordinates} \times R^T$$
6. Return a tuple containing: `(rotation_determinant, aligned_coordinates)`.

#### Example Walkthrough
```python
import numpy as np

coords = np.array([
    [10.0, 0.0],
    [0.0, 10.0],
    [10.0, 10.0]
])
offset = np.array([-5.0, 5.0])
angle = 90.0

det, aligned = align_customer_coordinates(coords, angle, offset)
print(det)  # Output: 1.0 (very close to 1.0)
print(np.round(aligned))
# Step 1: Translate -> [[5.0, 5.0], [-5.0, 15.0], [5.0, 15.0]]
# Step 2: Rotate 90 deg -> [[-5.0, 5.0], [-15.0, -5.0], [-15.0, 5.0]]
```
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
