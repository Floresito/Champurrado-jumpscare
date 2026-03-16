from __future__ import annotations

import random
import sys
from pathlib import Path
import tkinter as tk

import pillow_heif
from PIL import Image, ImageDraw, ImageFont, ImageTk

APP_NAME = "Champurrado Jumpscare"
PROBABILITY_PERCENT = 0.000001
CHECK_INTERVAL_MS = 1000
POPUP_DURATION_MS = 6000

pillow_heif.register_heif_opener()


class ChampurradoJumpscareApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.withdraw()
        self.rng = random.SystemRandom()
        self.active_popups: list[tk.Toplevel] = []

    @property
    def probability_per_second(self) -> float:
        return PROBABILITY_PERCENT / 100

    def run(self) -> None:
        self.schedule_check()
        self.root.mainloop()

    def schedule_check(self) -> None:
        if self.rng.random() < self.probability_per_second:
            self.show_popup()
        self.root.after(CHECK_INTERVAL_MS, self.schedule_check)

    def show_popup(self) -> None:
        window = tk.Toplevel(self.root)
        window.title(APP_NAME)
        window.configure(bg="black")
        window.attributes("-topmost", True)
        window.attributes("-fullscreen", True)

        image = self.load_champurrado_image(window.winfo_screenwidth(), window.winfo_screenheight())
        photo = ImageTk.PhotoImage(image)

        panel = tk.Label(window, image=photo, bg="black")
        panel.image = photo
        panel.pack(expand=True)

        close_action = lambda event=None: self.close_popup(window)
        window.bind("<Escape>", close_action)
        window.bind("<Button-1>", close_action)

        self.active_popups.append(window)
        window.after(POPUP_DURATION_MS, close_action)

    def close_popup(self, window: tk.Toplevel) -> None:
        if window in self.active_popups:
            self.active_popups.remove(window)
        if window.winfo_exists():
            window.destroy()

    def load_champurrado_image(self, screen_width: int, screen_height: int) -> Image.Image:
        candidates = self.candidate_image_paths()
        if candidates:
            image = Image.open(self.rng.choice(candidates)).convert("RGB")
            return self.fit_image_to_screen(image, screen_width, screen_height)

        placeholder = self.create_placeholder_image(screen_width, screen_height)
        return self.fit_image_to_screen(placeholder, screen_width, screen_height)

    def candidate_image_paths(self) -> list[Path]:
        valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".heic", ".heif"}

        base_paths = []
        if getattr(sys, "frozen", False):
            base_paths.append(Path(sys.executable).resolve().parent)
        else:
            base_paths.append(Path(__file__).resolve().parent.parent)

        candidates: list[Path] = []
        for base in base_paths:
            champurrado_dir = base / "assets" / "Champurrado"
            if champurrado_dir.exists() and champurrado_dir.is_dir():
                for file_path in champurrado_dir.iterdir():
                    if file_path.is_file() and file_path.suffix.lower() in valid_extensions:
                        candidates.append(file_path)

        return candidates

    def fit_image_to_screen(self, image: Image.Image, screen_width: int, screen_height: int) -> Image.Image:
        max_width = max(480, int(screen_width * 0.85))
        max_height = max(360, int(screen_height * 0.85))
        image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        return image

    def create_placeholder_image(self, screen_width: int, screen_height: int) -> Image.Image:
        width = max(640, int(screen_width * 0.7))
        height = max(480, int(screen_height * 0.7))
        image = Image.new("RGB", (width, height), color=(52, 30, 20))

        draw = ImageDraw.Draw(image)
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

        title = "CHAMPURRADO"
        subtitle = "Pon imágenes en assets/Champurrado"

        title_width = draw.textlength(title, font=title_font)
        subtitle_width = draw.textlength(subtitle, font=subtitle_font)

        draw.rectangle((40, 40, width - 40, height - 40), outline=(255, 214, 153), width=6)
        draw.text(((width - title_width) / 2, height * 0.40), title, fill=(255, 240, 220), font=title_font)
        draw.text(((width - subtitle_width) / 2, height * 0.55), subtitle, fill=(255, 240, 220), font=subtitle_font)

        return image


def main() -> None:
    app = ChampurradoJumpscareApp()
    app.run()


if __name__ == "__main__":
    main()
