"""
順運動学をPythonで実装する｜ロボットアームの手先位置を計算する

元記事: https://physical-ai.yurufuwa.work/learn/forward-kinematics-python
ゆるふわフィジカルAI (physical-ai.yurufuwa.work) の解説記事から抜粋したコードです。
"""

import numpy as np

def forward_kinematics(theta1, theta2, l1=1.0, l2=0.7):
    # 1つ目の関節の先（肘）の位置
    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)
    # 2つ目の関節の先（手先）= 肘 + 2リンク分。角度は累積(theta1+theta2)
    x2 = x1 + l2 * np.cos(theta1 + theta2)
    y2 = y1 + l2 * np.sin(theta1 + theta2)
    return (x1, y1), (x2, y2)

elbow, hand = forward_kinematics(np.radians(30), np.radians(45))
print("肘:", np.round(elbow, 3))
print("手先:", np.round(hand, 3))

reach = []
for t1 in np.linspace(0, np.pi, 30):
    for t2 in np.linspace(-np.pi, np.pi, 30):
        _, (hx, hy) = forward_kinematics(t1, t2)
        reach.append((hx, hy))

reach = np.array(reach)
print("手先が届く範囲: x", np.round(reach[:,0].min(),2), "〜", np.round(reach[:,0].max(),2))
print("最大リーチ:", round(np.max(np.hypot(reach[:,0], reach[:,1])), 3))  # ≈ l1+l2 = 1.7
