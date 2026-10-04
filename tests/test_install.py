import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "install.py"
SPEC = importlib.util.spec_from_file_location("installer", SCRIPT)
INSTALLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALLER)


class InstallTests(unittest.TestCase):
    def test_each_host_receives_the_complete_standalone_skill(self):
        for host, folder in (("claude", ".claude"), ("codex", ".agents")):
            with self.subTest(host=host), tempfile.TemporaryDirectory() as temporary:
                project = Path(temporary) / "project with spaces"
                project.mkdir()
                result = subprocess.run(
                    [sys.executable, str(SCRIPT), "--host", host, "--project", str(project)],
                    capture_output=True, text=True,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                target = project / folder / "skills" / INSTALLER.SKILL_NAME
                self.assertEqual(INSTALLER.inventory(INSTALLER.SOURCE), INSTALLER.inventory(target))
                self.assertEqual(set(project.iterdir()), {project / folder})

    def test_identical_reinstall_preserves_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "skill"
            INSTALLER.install(INSTALLER.SOURCE, target)
            before = (target / "SKILL.md").stat().st_mtime_ns
            INSTALLER.install(INSTALLER.SOURCE, target)
            self.assertEqual((target / "SKILL.md").stat().st_mtime_ns, before)

    def test_modified_or_extra_files_are_not_overwritten(self):
        for change in ("modified", "extra"):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as temporary:
                target = Path(temporary) / "skill"
                INSTALLER.install(INSTALLER.SOURCE, target)
                changed = target / ("SKILL.md" if change == "modified" else "personal-notes.md")
                changed.write_text("Keep my work", encoding="utf-8")
                before = INSTALLER.inventory(target)
                with self.assertRaises(ValueError):
                    INSTALLER.install(INSTALLER.SOURCE, target)
                self.assertEqual(INSTALLER.inventory(target), before)

    def test_symlink_installation_is_left_intact(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "skill"
            target.symlink_to(INSTALLER.SOURCE, target_is_directory=True)
            with self.assertRaises(ValueError):
                INSTALLER.install(INSTALLER.SOURCE, target)
            self.assertTrue(target.is_symlink())

    def test_nonexistent_project_is_not_created(self):
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "misspelled-project"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--host", "claude", "--project", str(project)],
                capture_output=True, text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(project.exists())


if __name__ == "__main__":
    unittest.main()
