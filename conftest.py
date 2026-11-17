
from pathlib import Path
import re

import pytest
from playwright.sync_api import sync_playwright
import pytest_html
from config import BASE_URL

ARTIFACTS_DIR = Path("test_artifacts")
ARTIFACTS_DIR.mkdir(exist_ok=True)


@pytest.fixture(scope="function")
def page(request):
    video_dir = ARTIFACTS_DIR / "videos"
    video_dir.mkdir(parents=True, exist_ok=True)

    test_name = re.sub(
        r"[^A-Za-z0-9_.-]+", "_", request.node.nodeid
    )

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(video_dir),
        viewport={"width": 1440, "height": 900},
    )

    page = context.new_page()
    saved_video = video_dir / f"{test_name}.webm"
    request.node.video_path = saved_video

    try:
        page.goto(BASE_URL, wait_until="domcontentloaded")
        page.wait_for_load_state("domcontentloaded")

        yield page

    finally:
        context.close()

        generated_video = Path(page.video.path())

        if generated_video.exists():
            if generated_video.resolve() != saved_video.resolve():
                generated_video.replace(saved_video)

            request.node.video_path = saved_video

        browser.close()
        p.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = list(getattr(report, "extras", []))

    if report.when == "call":
        video_path = getattr(item, "video_path", None)
        if video_path:
            relative_video_path = video_path.resolve().relative_to(
                Path.cwd().resolve()
            ).as_posix()
            extra.append(
                pytest_html.extras.html(
                    f"<a href='{relative_video_path}' target='_blank'>"
                    f"{item.name} - Open Video</a><br>"
                    f"<video controls preload='metadata' width='640'>"
                    f"<source src='{relative_video_path}' type='video/webm'>"
                    f"</video>"
                )
            )

    report.extras = extra


    report.extras = extra
