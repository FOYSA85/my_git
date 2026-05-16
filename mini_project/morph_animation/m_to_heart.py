import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon, Circle

# =========================================================
# Curve helpers
# =========================================================
def catmull_rom_closed(points, samples_per_seg=120):
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
    pts = np.asarray(points, dtype=float)

    y = pts[:, 1]

    thresh = np.quantile(y, bottom_fraction)

    cand = np.where(y <= thresh)[0]

    if len(cand) == 0:
        return pts

    idx = cand[np.argmin(np.abs(pts[cand, 0]))]

    return np.roll(pts, -idx, axis=0)


def best_cyclic_alignment(ref, pts):
    n = len(ref)

    best = pts
    best_err = np.inf

    for candidate in (pts, pts[::-1]):

        for shift in range(n):

            rolled = np.roll(candidate, shift, axis=0)

            err = np.mean((ref - rolled) ** 2)

            if err < best_err:
                best_err = err
                best = rolled

    return best


def ease_in_out_quint(x):
    x = np.clip(x, 0.0, 1.0)

    return (
        16 * x**5
        if x < 0.5
        else 1 - (-2 * x + 2) ** 5 / 2
    )


def rotate_scale(points, angle_deg=0.0, scale=1.0):
    pts = np.asarray(points, dtype=float)

    theta = np.deg2rad(angle_deg)

    c, s = np.cos(theta), np.sin(theta)

    R = np.array([
        [c, -s],
        [s,  c]
    ])

    return (pts @ R.T) * scale


# =========================================================
# Animated neon gradient
# =========================================================
def gradient_color(t):

    c1 = np.array([0.20, 0.95, 1.00])   # cyan
    c2 = np.array([1.00, 0.35, 0.75])   # pink
    c3 = np.array([0.72, 0.35, 1.00])   # violet

    if t < 0.5:
        u = t * 2
        c = (1 - u) * c1 + u * c2
    else:
        u = (t - 0.5) * 2
        c = (1 - u) * c2 + u * c3

    return tuple(c)


# =========================================================
# M shape
# =========================================================
M_CTRL = np.array([
    [-1.12, -1.10],
    [-1.22, -0.20],
    [-1.15,  0.75],
    [-0.92,  1.18],
    [ 0.00,  0.12],
    [ 0.92,  1.18],
    [ 1.15,  0.75],
    [ 1.22, -0.20],
    [ 1.12, -1.10],
    [ 0.72, -1.00],
    [ 0.68, -0.15],
    [ 0.48,  0.10],
    [ 0.00, -0.55],
    [-0.48,  0.10],
    [-0.68, -0.15],
    [-0.72, -1.00],
], dtype=np.float64)


# =========================================================
# Heart curve
# =========================================================
def perfect_heart(num=7000):

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


# =========================================================
# Prepare shapes
# =========================================================
N = 2400

m_dense = catmull_rom_closed(M_CTRL, samples_per_seg=180)
m_shape = resample_closed_curve(m_dense, N)
m_shape = normalize_to_box(m_shape, target=1.35)

h_dense = perfect_heart(7000)
h_shape = resample_closed_curve(h_dense, N)
h_shape = normalize_to_box(h_shape, target=1.35)

m_shape = rotate_start_near_bottom_center(m_shape)
h_shape = rotate_start_near_bottom_center(h_shape)

if np.sign(signed_area(m_shape)) != np.sign(signed_area(h_shape)):
    h_shape = h_shape[::-1]

h_shape = best_cyclic_alignment(m_shape, h_shape)

# =========================================================
# Background particles
# =========================================================
rng = np.random.default_rng(7)

particle_n = 90

particle_angles = rng.uniform(0, 2 * np.pi, particle_n)
particle_r = rng.uniform(1.4, 2.7, particle_n)

particle_phase = rng.uniform(0, 2 * np.pi, particle_n)
particle_speed = rng.uniform(0.35, 1.20, particle_n)

particle_size = rng.uniform(12, 65, particle_n)

px0 = particle_r * np.cos(particle_angles)
py0 = particle_r * np.sin(particle_angles)

# =========================================================
# Figure setup
# =========================================================
fig, ax = plt.subplots(
    figsize=(8, 8),
    facecolor="black"
)

ax.set_facecolor("black")

ax.set_aspect("equal")

ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

ax.axis("off")

# =========================================================
# Aurora cinematic background
# =========================================================
grid = 700

xx = np.linspace(-2.4, 2.4, grid)
yy = np.linspace(-2.4, 2.4, grid)

X, Y = np.meshgrid(xx, yy)

R = np.sqrt(X**2 + Y**2)

bg1 = np.exp(-((X + 0.6)**2 + (Y - 0.4)**2) * 1.6)
bg2 = np.exp(-((X - 0.7)**2 + (Y + 0.5)**2) * 1.2)
bg3 = np.exp(-(R**2) * 0.9)

aurora = np.zeros((grid, grid, 3))

aurora[..., 0] = 0.95 * bg2 + 0.25 * bg3
aurora[..., 1] = 0.70 * bg1 + 0.15 * bg2
aurora[..., 2] = 1.00 * bg1 + 0.95 * bg3

aurora = np.clip(aurora, 0, 1)

ax.imshow(
    aurora,
    extent=[-2.4, 2.4, -2.4, 2.4],
    origin="lower",
    alpha=0.42,
    zorder=0
)

# =========================================================
# Halo ring
# =========================================================
halo = Circle(
    (0, 0),
    1.45,
    fill=False,
    lw=2.0,
    alpha=0.10,
)

ax.add_patch(halo)

# =========================================================
# Fill glow
# =========================================================
fill_patch = Polygon(
    m_shape,
    closed=True,
    facecolor=gradient_color(0.5),
    edgecolor="none",
    alpha=0.06,
    zorder=2
)

ax.add_patch(fill_patch)

# =========================================================
# Neon glow layers
# =========================================================
glow1, = ax.plot(
    [],
    [],
    lw=34,
    alpha=0.025,
    solid_capstyle="round",
    zorder=3
)

glow2, = ax.plot(
    [],
    [],
    lw=24,
    alpha=0.05,
    solid_capstyle="round",
    zorder=4
)

glow3, = ax.plot(
    [],
    [],
    lw=14,
    alpha=0.12,
    solid_capstyle="round",
    zorder=5
)

glow4, = ax.plot(
    [],
    [],
    lw=8,
    alpha=0.22,
    solid_capstyle="round",
    zorder=6
)

line, = ax.plot(
    [],
    [],
    lw=3.2,
    solid_capstyle="round",
    zorder=7
)

# =========================================================
# Particles
# =========================================================
sc = ax.scatter(
    px0,
    py0,
    s=particle_size,
    c=np.ones((particle_n, 4)),
    alpha=0.0,
    zorder=1
)

# =========================================================
# Pulse center
# =========================================================
pulse_dot = ax.scatter(
    [0],
    [0],
    s=0,
    c=[gradient_color(0.5)],
    alpha=0.0,
    zorder=8
)

# =========================================================
# Text
# =========================================================
ax.text(
    0.5,
    1.18,
    "M → Heart",
    transform=ax.transAxes,
    ha="center",
    va="center",
    color="white",
    fontsize=26,
    fontweight="bold"
)

ax.text(
    0.5,
    1.05,
    "Cinematic Neon Morph",
    transform=ax.transAxes,
    ha="center",
    va="center",
    color="white",
    fontsize=14,
    alpha=0.85
)

pct_text = ax.text(
    0.5,
    1.085,
    "0%",
    transform=ax.transAxes,
    ha="center",
    va="center",
    color="white",
    fontsize=18
)

# =========================================================
# Animation update
# =========================================================
def update(frame):

    phase = (frame % 420) / 420.0

    # smooth morph
    t = phase if phase <= 0.5 else 1.0 - phase
    t *= 2.0

    t = ease_in_out_quint(t)

    # breathing
    breath = 1.0 + 0.025 * np.sin(
        2 * np.pi * phase * 2.0
    )

    # tiny rotation drift
    drift_angle = 2.2 * np.sin(
        2 * np.pi * phase
    )

    wobble = 0.01 * np.sin(
        2 * np.pi * phase * 3.0
    )

    # morph interpolation
    pts = (1 - t) * m_shape + t * h_shape

    # transform
    pts = rotate_scale(
        pts,
        angle_deg=drift_angle,
        scale=breath
    )

    pts[:, 1] += wobble * (0.35 + 0.65 * t)

    x = pts[:, 0]
    y = pts[:, 1]

    # =====================================================
    # Animated neon gradient
    # =====================================================
    dynamic_color = gradient_color(
        0.5 + 0.5 * np.sin(
            2 * np.pi * phase
        )
    )

    brightness = 0.75 + 0.35 * np.sin(np.pi * t)

    dynamic_color = tuple(
        np.clip(
            np.array(dynamic_color) * brightness,
            0,
            1
        )
    )

    # =====================================================
    # Glow update
    # =====================================================
    for artist in (
        glow1,
        glow2,
        glow3,
        glow4,
        line
    ):
        artist.set_data(x, y)
        artist.set_color(dynamic_color)

    # =====================================================
    # Fill update
    # =====================================================
    fill_patch.set_xy(
        np.column_stack([x, y])
    )

    fill_patch.set_facecolor(dynamic_color)

    fill_patch.set_alpha(
        0.045
        + 0.065
        * (0.5 + 0.5 * np.sin(np.pi * t))
    )

    # =====================================================
    # Halo animation
    # =====================================================
    halo.set_edgecolor(dynamic_color)

    halo.set_alpha(
        0.06
        + 0.07
        * (np.sin(np.pi * t) ** 2)
    )

    halo.set_linewidth(
        1.7
        + 1.4
        * (np.sin(np.pi * t) ** 2)
    )

    # =====================================================
    # Pulse center
    # =====================================================
    pulse_size = (
        30
        + 260
        * (np.sin(np.pi * t) ** 2)
    )

    pulse_alpha = (
        0.08
        + 0.16
        * (np.sin(np.pi * t) ** 2)
    )

    pulse_dot.set_sizes([pulse_size])

    pulse_dot.set_alpha(pulse_alpha)

    pulse_dot.set_color([dynamic_color])

    # =====================================================
    # Particles
    # =====================================================
    pa = phase * 2 * np.pi

    px = px0 + 0.03 * np.sin(
        pa * particle_speed + particle_phase
    )

    py = py0 + 0.03 * np.cos(
        pa * (particle_speed * 0.8)
        + particle_phase * 1.3
    )

    offsets = np.column_stack([px, py])

    sc.set_offsets(offsets)

    alphas = (
        0.15
        + 0.55
        * (
            0.5
            + 0.5
            * np.sin(
                pa * particle_speed
                + particle_phase
            )
        )
    )

    sizes = particle_size * (
        0.75
        + 0.65
        * (
            0.5
            + 0.5
            * np.sin(
                pa * particle_speed * 1.15
                + particle_phase
            )
        )
    )

    colors = np.ones((particle_n, 4))

    colors[:, 0] = dynamic_color[0]
    colors[:, 1] = dynamic_color[1]
    colors[:, 2] = dynamic_color[2]

    colors[:, 3] = np.clip(
        alphas * 0.35,
        0,
        0.35
    )

    sc.set_facecolors(colors)

    sc.set_sizes(sizes)

    # =====================================================
    # Percentage
    # =====================================================
    pct_text.set_text(
        f"{int(round(t * 100))}%"
    )

    return (
        glow1,
        glow2,
        glow3,
        glow4,
        line,
        fill_patch,
        sc,
        pulse_dot,
        halo,
        pct_text
    )


# =========================================================
# Run animation
# =========================================================
anim = FuncAnimation(
    fig,
    update,
    frames=420,
    interval=18,
    blit=True
)

plt.show()
