#!/usr/bin/env python3
"""Regression tests for prototype control flow and safety boundaries."""

from __future__ import annotations

import importlib.util
import pathlib
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载模块: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


reflexion = load_module(
    "prototype_reflexion",
    "practices/prototypes/reflexion/reflexion.py",
)
voyager = load_module(
    "prototype_voyager_skill",
    "practices/prototypes/voyager_skill/voyager_skill.py",
)
self_refine = load_module(
    "prototype_self_refine",
    "practices/prototypes/self_refine/self_refine.py",
)


class ReflexionTests(unittest.TestCase):
    def test_candidate_code_runs_in_child_process(self):
        code = """
def is_prime(n):
    if n <= 1:
        return False
    return all(n % i for i in range(2, int(n ** 0.5) + 1))
"""
        passed, diagnostic = reflexion.run_tests(
            code,
            reflexion.DEFAULT_TESTS,
            timeout=2,
        )
        self.assertTrue(passed, diagnostic)

    def test_candidate_timeout_is_reported(self):
        passed, diagnostic = reflexion.run_tests(
            "while True: pass",
            [],
            timeout=0.1,
        )
        self.assertFalse(passed)
        self.assertIn("超时", diagnostic)


class VoyagerTests(unittest.TestCase):
    def test_fail_text_containing_pass_is_not_accepted(self):
        passed, response = voyager._verify(
            lambda _prompt: "FAIL: the answer does not PASS validation",
            "task",
            "solution",
        )
        self.assertFalse(passed)
        self.assertTrue(response.startswith("FAIL"))

    def test_failed_solution_is_retried_with_feedback(self):
        state = {"verify": 0, "solve": 0}

        def fake_llm(prompt: str) -> str:
            if prompt.startswith("VERIFY"):
                state["verify"] += 1
                return "FAIL: missing detail" if state["verify"] == 1 else "PASS"
            if prompt.startswith("ABSTRACT"):
                return "Skill: reusable corrected solution"
            state["solve"] += 1
            return f"solution-{state['solve']}"

        library = voyager.SkillLibrary()
        result = voyager.solve_task("task", fake_llm, library, retries=1)

        self.assertTrue(result.passed)
        self.assertEqual(result.attempts, 2)
        self.assertEqual(result.solution, "solution-2")
        self.assertEqual(len(library.skills), 1)


class SelfRefineTests(unittest.TestCase):
    def test_satisfied_feedback_with_improvement_request_does_not_stop(self):
        self.assertFalse(self_refine._looks_satisfied("很好,但应该加入一个例子。"))
        self.assertTrue(self_refine._looks_satisfied("很好,无需修改。"))


if __name__ == "__main__":
    unittest.main()
