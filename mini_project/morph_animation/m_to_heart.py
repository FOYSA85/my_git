import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------------------
# Curve helpers
# ----------------------------
def catmull_rom_closed(points, samples_per_seg=80):
    pts = np.asarray(points, dtype=float)
    n = len(pts)
    out = []

    for i in range(n):
        p0 = pts[(i - 1) % n]
        p1 = pts[i % n]
        p2 = pts[(i + 1) % n]
        p3 = pts[(i + 2) % n]

        b0 = p1
        b1 = p1 + (p2 - p0) / 6.0
        b2 = p2 - (p3 - p1) / 6.0
        b3 = p2

        t = np.linspace(0, 1, samples_per_seg, endpoint=False)
        mt = 1 - t

        seg = (
            (mt**3)[:, None] * b0
            + (3 * mt**2 * t)[:, None] * b1
            + (3 * mt * t**2)[:, None] * b2
            + (t**3)[:, None] * b3
        )

        out.append(seg)

    curve = np.vstack(out)
    return np.vstack([curve, curve[0]])


def resample_closed_curve(points, n):
    pts = np.asarray(points, dtype=float)

    if np.allclose(pts[0], pts[-1]):
        pts = pts[:-1]

    pts2 = np.vstack([pts, pts[0]])

    seg = np.linalg.norm(np.diff(pts2, axis=0), axis=1)
    cum = np.concatenate([[0.0], np.cumsum(seg)])
    total = cum[-1]

    targets = np.linspace(0, total, n, endpoint=False)

    out = np.empty((n, 2), dtype=float)

    for i, d in enumerate(targets):
        idx = np.searchsorted(cum, d, side="right") - 1
        idx = np.clip(idx, 0, len(pts2) - 2)

        d0, d1 = cum[idx], cum[idx + 1]

        t = 0.0 if d1 == d0 else (d - d0) / (d1 - d0)

        out[i] = pts2[idx] * (1 - t) + pts2[idx + 1] * t

    return out


def normalize_to_box(points, target=1.35):
    pts = np.asarray(points, dtype=float)

    pts = pts - pts.mean(axis=0)

    span = np.max(np.ptp(pts, axis=0))

    if span == 0:
        return pts

    return pts * (target / span)


def signed_area(points):
    pts = np.asarray(points, dtype=float)

    if np.allclose(pts[0], pts[-1]):
        pts = pts[:-1]

    x, y = pts[:, 0], pts[:, 1]

    return 0.5 * np.sum(
        x * np.roll(y, -1) - np.roll(x, -1) * y
    )


def rotate_start_near_bottom_center(points, bottom_fraction=0.30):
    """
    Contour seam bottom-center এর কাছাকাছি আনে
    যাতে morph symmetric হয়।
    """
    pts = np.asarray(points, dtype=float)

    y = pts[:, 1]

    thresh = np.quantile(y, bottom_fraction)

    cand = np.where(y <= thresh)[0]

    if len(cand) == 0:
        return pts

    idx = cand[np.argmin(np.abs(pts[cand, 0]))]

    return np.roll(pts, -idx, axis=0)


def best_cyclic_alignment(ref, pts):
    """
    ref shape এর সাথে pts shape এর best cyclic alignment বের করে।
    এতে left/right twisting কমে যায়।
    """
    n = len(ref)

    best = pts
    best_err = np.inf

    # normal + reversed দুইটাই test করি
    for candidate in (pts, pts[::-1]):

        # সব possible cyclic shift
        for shift in range(n):

            rolled = np.roll(candidate, shift, axis=0)

            err = np.mean((ref - rolled) ** 2)

            if err < best_err:
                best_err = err
                best = rolled

    return best


def ease_in_out_sine(x):
    return 0.5 - 0.5 * np.cos(np.pi * x)


# ----------------------------
# M outline
# ----------------------------
M_CTRL = np.array([

    # LEFT OUTER SIDE
    [-1.12, -1.10],
    [-1.22,  -.20],
    [-1.15,  0.75],
    [-0.92,  1.18],

    # TOP CENTER VALLEY
    [ 0.00,  0.12],

    # RIGHT OUTER SIDE
    [ 0.92,  1.18],
    [ 1.15,  0.75],
    [ 1.22, -0.20],
    [ 1.12, -1.10],

    # RIGHT INNER STEM
    [ 0.72, -1.00],
    [ 0.68, -0.15],
    [ 0.48,  0.10],

    # INNER CENTER VALLEY
    [ 0.00, -0.55],

    # LEFT INNER STEM
    [-0.48,  0.10],
    [-0.68, -0.15],
    [-0.72, -1.00],
])


# ----------------------------
# Perfect heart curve
# ----------------------------
def perfect_heart(num=4000):

    t = np.linspace(0, 2 * np.pi, num, endpoint=False)

    x = 16 * np.sin(t) ** 3

    y = (
        13 * np.cos(t)
        - 5 * np.cos(2 * t)
        - 2 * np.cos(3 * t)
        - np.cos(4 * t)
    )

    pts = np.column_stack([x, y])

    pts[:, 0] /= 16.0
    pts[:, 1] /= 17.0

    pts[:, 1] *= 1.05

    return pts


# ----------------------------
# Prepare shapes
# ----------------------------
N = 1400

# M shape
m_dense = catmull_rom_closed(M_CTRL, samples_per_seg=100)
m_shape = resample_closed_curve(m_dense, N)
m_shape = normalize_to_box(m_shape, target=1.35)

# Heart shape
h_dense = perfect_heart(5000)
h_shape = resample_closed_curve(h_dense, N)
h_shape = normalize_to_box(h_shape, target=1.35)

# Seam alignment
m_shape = rotate_start_near_bottom_center(
    m_shape,
    bottom_fraction=0.30
)

h_shape = rotate_start_near_bottom_center(
    h_shape,
    bottom_fraction=0.30
)

# Orientation fix
if np.sign(signed_area(m_shape)) != np.sign(signed_area(h_shape)):
    h_shape = h_shape[::-1]

# Best cyclic alignment
h_shape = best_cyclic_alignment(m_shape, h_shape)


# ----------------------------
# Animation setup
# ----------------------------
fig, ax = plt.subplots(
    figsize=(8, 8),
    facecolor="black"
)

ax.set_facecolor("black")

ax.set_aspect("equal")

ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.7, 1.7)

ax.axis("off")

line_color = "#ff88cc"

# Glow layers
glow1, = ax.plot(
    [], [],
    color=line_color,
    lw=26,
    alpha=0.03,
    solid_capstyle="round"
)

glow2, = ax.plot(
    [], [],
    color=line_color,
    lw=18,
    alpha=0.06,
    solid_capstyle="round"
)

glow3, = ax.plot(
    [], [],
    color=line_color,
    lw=12,
    alpha=0.10,
    solid_capstyle="round"
)

glow4, = ax.plot(
    [], [],
    color=line_color,
    lw=7,
    alpha=0.18,
    solid_capstyle="round"
)

line, = ax.plot(
    [], [],
    color=line_color,
    lw=3.2,
    solid_capstyle="round"
)

# Percentage text
pct_text = ax.text(
    0.5,
    1.08,
    "0%",
    transform=ax.transAxes,
    ha="center",
    va="center",
    color="white",
    fontsize=18
)

# Title
ax.text(
    0.5,
    1.18,
    "M → Heart",
    transform=ax.transAxes,
    ha="center",
    va="center",
    color="#ff9fd8",
    fontsize=24,
    fontweight="bold"
)

# Subtitle
ax.text(
    0.5,
    1.05,
    "Smooth morph animation",
    transform=ax.transAxes,
    ha="center",
    va="center",
    color="white",
    fontsize=14,
    alpha=0.9
)


# ----------------------------
# Animation update
# ----------------------------
def update(frame):

    phase = (frame % 240) / 240.0

    # forward + backward
    t = phase if phase <= 0.5 else 1.0 - phase

    t *= 2.0

    # easing
    t = ease_in_out_sine(t)

    # morph
    pts = (1 - t) * m_shape + t * h_shape

    x = pts[:, 0]
    y = pts[:, 1]

    # update all glow layers
    for artist in (
        glow1,
        glow2,
        glow3,
        glow4,
        line
    ):
        artist.set_data(x, y)

    pct_text.set_text(f"{int(round(t * 100))}%")

    return (
        glow1,
        glow2,
        glow3,
        glow4,
        line,
        pct_text
    )


# ----------------------------
# Run animation
# ----------------------------
anim = FuncAnimation(
    fig,
    update,
    frames=240,
    interval=25,
    blit=True
)

plt.show()
