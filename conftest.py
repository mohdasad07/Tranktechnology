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
    video_dir.mkdir(exist_ok=True)
    test_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", request.node.nodeid)

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(video_dir),
        viewport={"width": 1440, "height": 900},
    )

    page = context.new_page()

    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.wait_for_load_state("domcontentloaded")

    yield page

    context.close()
    generated_video = Path(page.video.path())
    saved_video = video_dir / f"{test_name}.webm"
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

    # Screenshot attachment
    if report.when == "call":
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            try:
                page.screenshot(path=str(file_name), full_page=True)
                extra.append(
                    pytest_html.extras.image(str(file_name))
                )
            except Exception as exc:
                print(f"Unable to save screenshot: {exc}")

    # Video attachment after fixture teardown
    if report.when == "teardown":
        video_path = getattr(item, "video_path", None)

        if video_path and video_path.exists():
            relative_video_path = video_path.resolve().relative_to(
                Path.cwd()
            )

            extra.append(
                pytest_html.extras.html(
                    f"<a href='{relative_video_path.as_posix()}' "
                    f"target='_blank'>{item.name} - Open video</a><br>"
                    f"""
                    <video width="640" height="360" controls>
                        <source src="{relative_video_path.as_posix()}"
                        type="video/webm">
                    </video>
                    """
                )
            )

    report.extras = extra
