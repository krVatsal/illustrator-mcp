import unittest

from illustrator import prompt


class PromptTests(unittest.TestCase):
    def test_get_prompt_suggestions_returns_categories(self):
        suggestions = prompt.get_prompt_suggestions()
        self.assertIsInstance(suggestions, dict)
        self.assertGreater(len(suggestions), 0)

    def test_format_advanced_template(self):
        result = prompt.format_advanced_template(
            "logo_design",
            company_name="Acme",
            industry="technology",
            style="minimalist",
            colors="blue and white",
            elements="lettermark",
            size="1024x1024",
        )
        self.assertIn("Acme", result)

    def test_unknown_template_raises_value_error(self):
        with self.assertRaises(ValueError):
            prompt.format_advanced_template("missing_template")


if __name__ == "__main__":
    unittest.main()
