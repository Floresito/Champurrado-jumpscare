from __future__ import annotations

import random
import sys
import time
from pathlib import Path

import pygame
import pillow_heif
from PIL import Image, ImageDraw, ImageFont

APP_NAME = "Champurrado Jumpscare"
PROBABILITY_PERCENT = 0.000001
CHECK_INTERVAL_SECONDS = 1
POPUP_DURATION_MS = 6000

pillow_heif.register_heif_opener()


class ChampurradoJumpscareApp:
    def __init__(self) -> None:
        self.rng = random.SystemRandom()

    @property
    def probability_per_second(self) -> float:
        return PROBABILITY_PERCENT / 100

    def run(self) -> None:
        while True:
            if self.rng.random() < self.probability_per_second:
                self.show_popup()
            time.sleep(CHECK_INTERVAL_SECONDS)

    def show_popup(self) -> None:
        pygame.init()
        try:
            display_info = pygame.display.Info()
            screen_width = display_info.current_w
            screen_height = display_info.current_h

            flags = pygame.FULLSCREEN | pygame.NOFRAME
            screen = pygame.display.set_mode((screen_width, screen_height), flags)
            pygame.display.set_caption(APP_NAME)

            image = self.load_champurrado_image(screen_width, screen_height)
            image_surface = self.pil_to_surface(image)

            screen.fill((0, 0, 0))
            image_rect = image_surface.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(image_surface, image_rect)
            pygame.display.flip()

            start = time.monotonic()
            duration_seconds = POPUP_DURATION_MS / 1000
            while time.monotonic() - start < duration_seconds:
                for event in pygame.event.get():
                    if event.type in (pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                        return
                time.sleep(0.01)
        finally:
            pygame.display.quit()
            pygame.quit()

    def pil_to_surface(self, image: Image.Image) -> pygame.Surface:
        rgb_image = image.convert("RGB")
        return pygame.image.fromstring(rgb_image.tobytes(), rgb_image.size, "RGB")

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
