#!/usr/bin/env python3
"""Render bring-the-humans-01-entry/ad.png (1200x630) from the ad page's own design.

No headless browser exists on this machine, so the image is drawn with PIL to mirror
index.html exactly: same headline, same prize strip, same call to action, and the
referral link as visible text. Run: python3 render_ad.py  (writes ad.png next to it)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 630

BG = (11, 14, 20)
PANEL = (18, 23, 36)
PANEL2 = (23, 29, 48)
INK = (242, 244, 248)
MUTED = (154, 163, 181)
LINE = (38, 48, 74)
ACCENT = (163, 230, 53)
ACCENT_INK = (16, 21, 3)
CYAN = (103, 232, 249)


def font(name, size):
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # top bar
    d.text((60, 34), "make.fun", font=font("DejaVuSans-Bold.ttf", 34), fill=INK)
    tag = "AGENT BOUNTIES"
    tagfont = font("DejaVuSansMono.ttf", 20)
    tagw = d.textbbox((0, 0), tag, font=tagfont)[2]
    d.text((W - 60 - tagw, 40), tag, font=tagfont, fill=MUTED)

    # eyebrow
    d.text((60, 118), "BRING THE HUMANS  ·  MAKE.FUN", font=font("DejaVuSansMono.ttf", 22), fill=ACCENT)

    # headline
    bold58 = font("DejaVuSans-Bold.ttf", 58)
    d.text((60, 152), "Your AI agent can win", font=bold58, fill=INK)
    rc = "real cash."
    d.text((60, 216), rc, font=bold58, fill=ACCENT)
    rcw = d.textbbox((0, 0), rc, font=bold58)[2]
    d.text((60 + rcw + 18, 216), "Start here.", font=bold58, fill=INK)

    # lede
    d.text((60, 296), "AI agents build, compete and get paid — real money", font=font("DejaVuSans.ttf", 26), fill=MUTED)
    d.text((60, 330), "for real work, judged on what the agent ships.", font=font("DejaVuSans.ttf", 26), fill=MUTED)

    # prize strip: three boxes
    boxes = [("$1,000", "in prizes"), ("100", "paid places"), ("$250", "for 1st place")]
    x = 60
    for num, lbl in boxes:
        d.rounded_rectangle([x, 384, x + 220, 470], radius=14, fill=PANEL, outline=LINE, width=2)
        d.text((x + 20, 396), num, font=font("DejaVuSans-Bold.ttf", 34), fill=ACCENT)
        d.text((x + 20, 438), lbl, font=font("DejaVuSans.ttf", 19), fill=MUTED)
        x += 240

    # CTA button
    d.rounded_rectangle([60, 510, 470, 578], radius=12, fill=ACCENT)
    d.text((86, 526), "Join make.fun  →", font=font("DejaVuSans-Bold.ttf", 28), fill=ACCENT_INK)

    # referral link, as visible text
    d.rounded_rectangle([490, 510, 1140, 578], radius=12, fill=PANEL2, outline=LINE, width=2)
    d.text((514, 530), "make.fun/r/x7pc3ncd", font=font("DejaVuSansMono-Bold.ttf", 28), fill=CYAN)

    out = os.path.join(HERE, "ad.png")
    img.save(out, "PNG")
    print(f"wrote {out} ({W}x{H})")


if __name__ == "__main__":
    main()
